import multiprocessing
import time
import logging
from typing import List, Dict
from guess_a_hash import time_to_find_hashed_string_value
from metrics import PipelineMetrics, MetricsCollector
from config import PipelineConfig

def setup_logging(config: PipelineConfig) -> logging.Logger:
    """Configure process-safe logging."""
    logging.basicConfig(
        level=getattr(logging, config.log_level),
        format=config.log_format
    )
    return logging.getLogger(__name__)

def cpu_bound_task(string_name: str, config: PipelineConfig, result_queue: multiprocessing.Queue) -> None:
    """
    Execute CPU-intensive hash finding in separate process.
    
    Args:
        string_name: Name of cryptocurrency to process
        config: Pipeline configuration
        result_queue: Queue for collecting metrics across processes
    """
    logger = setup_logging(config)
    process_name = multiprocessing.current_process().name
    metric = PipelineMetrics(task_name=string_name)
    
    logger.info(f"Process {process_name} for '{string_name}' started")
    
    try:
        value, duration, hash_string, attempts = time_to_find_hashed_string_value(string_name)
        metric.end_time = time.perf_counter()
        metric.attempts = attempts
        metric.success = True
        
        logger.info(
            f"Process {process_name} for '{string_name}' found target {hash_string} "
            f"of value {value} in {duration}s after {attempts} attempts"
        )
    except Exception as e:
        metric.end_time = time.perf_counter()
        metric.error_msg = str(e)
        logger.error(f"Process {process_name} for '{string_name}' failed: {e}")
    finally:
        result_queue.put(metric.to_dict())

def main() -> None:
    """Execute parallel hash finding across multiple processes with metrics collection."""
    config = PipelineConfig.from_env()
    logger = setup_logging(config)
    
    start_time = time.perf_counter()
    logger.info(
        f"Starting multiprocessing pipeline with {config.max_workers} CPU cores available, "
        f"processing {len(config.crypto_targets)} targets"
    )
    
    # Shared queue for cross-process metrics collection
    result_queue = multiprocessing.Queue()
    processes: List[multiprocessing.Process] = []
    
    # Create and start processes
    for crypto in config.crypto_targets:
        process = multiprocessing.Process(
            target=cpu_bound_task,
            args=(crypto, config, result_queue),
            name=f"Process-{crypto}"
        )
        process.start()
        processes.append(process)
    
    # Wait for completion
    for process in processes:
        process.join()
    
    # Collect metrics from all processes
    collector = MetricsCollector()
    while not result_queue.empty():
        metric_dict = result_queue.get()
        metric = PipelineMetrics(
            task_name=metric_dict['task'],
            attempts=metric_dict['attempts']
        )
        metric.end_time = metric.start_time + metric_dict['duration']
        metric.success = metric_dict['success']
        metric.error_msg = metric_dict['error']
        collector.add_metric(metric)
    
    # Log comprehensive summary
    summary = collector.summary()
    total_duration = round(time.perf_counter() - start_time, 2)
    
    logger.info(
        f"Pipeline execution completed in {total_duration}s - "
        f"Success: {summary.get('successful', 0)}/{summary.get('total_tasks', 0)}, "
        f"Avg Duration: {summary.get('avg_duration', 0)}s, "
        f"Total Attempts: {summary.get('total_attempts', 0)}, "
        f"Success Rate: {summary.get('success_rate', 0)}%"
    )

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows compatibility
    main()