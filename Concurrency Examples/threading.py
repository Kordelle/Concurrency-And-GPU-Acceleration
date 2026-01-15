import threading
import time
import logging
from typing import List
from guess_a_hash import time_to_find_hashed_string_value
from metrics import PipelineMetrics, MetricsCollector
from config import PipelineConfig

def setup_logging(config: PipelineConfig) -> logging.Logger:
    """Configure thread-safe logging."""
    logging.basicConfig(
        level=getattr(logging, config.log_level),
        format=config.log_format
    )
    return logging.getLogger(__name__)

def task(string_name: str, config: PipelineConfig, metrics_collector: MetricsCollector) -> None:
    """
    Execute hash finding task with metrics collection.
    Thread-safe metrics aggregation for production monitoring.
    """
    logger = setup_logging(config)
    thread_name = threading.current_thread().name
    metric = PipelineMetrics(task_name=string_name)
    
    logger.info(f"{thread_name} for '{string_name}' started")
    
    try:
        value, duration, hash_string, attempts = time_to_find_hashed_string_value(string_name)
        metric.end_time = time.perf_counter()
        metric.attempts = attempts
        metric.success = True
        
        logger.info(
            f"{thread_name} for '{string_name}' found target {hash_string} "
            f"of value {value} in {duration}s after {attempts} attempts"
        )
    except Exception as e:
        metric.end_time = time.perf_counter()
        metric.error_msg = str(e)
        logger.error(f"{thread_name} for '{string_name}' failed: {e}")
    finally:
        metrics_collector.add_metric(metric)

def main() -> None:
    """Execute threaded hash finding with metrics collection."""
    config = PipelineConfig.from_env()
    logger = setup_logging(config)
    collector = MetricsCollector()
    
    start_time = time.perf_counter()
    logger.info(f"Starting threading pipeline with {len(config.crypto_targets)} targets")
    
    threads: List[threading.Thread] = []
    
    for crypto in config.crypto_targets:
        thread = threading.Thread(
            target=task,
            args=(crypto, config, collector),
            name=f"Thread-{crypto}"
        )
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    summary = collector.summary()
    total_duration = round(time.perf_counter() - start_time, 2)
    
    logger.info(
        f"Threading pipeline completed in {total_duration}s - "
        f"Success: {summary.get('successful', 0)}/{summary.get('total_tasks', 0)}, "
        f"Avg Duration: {summary.get('avg_duration', 0)}s, "
        f"Success Rate: {summary.get('success_rate', 0)}%"
    )

if __name__ == '__main__':
    main()