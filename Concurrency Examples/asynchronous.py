import time
import asyncio
import logging
from typing import List
from guess_a_hash import time_to_find_hashed_string_value
from metrics import PipelineMetrics, MetricsCollector
from config import PipelineConfig

def setup_logging(config: PipelineConfig) -> logging.Logger:
    """Configure async-safe logging."""
    logging.basicConfig(
        level=getattr(logging, config.log_level),
        format=config.log_format
    )
    return logging.getLogger(__name__)

async def async_task(string_name: str, config: PipelineConfig) -> PipelineMetrics:
    """
    Execute hash finding asynchronously with metrics tracking.
    Production pattern: Non-blocking I/O for high-throughput event processing.
    """
    logger = setup_logging(config)
    metric = PipelineMetrics(task_name=string_name)
    
    logger.info(f"Starting async task for '{string_name}'")
    
    try:
        value, duration, hash_string, attempts = await asyncio.to_thread(
            time_to_find_hashed_string_value,
            string_name
        )
        metric.end_time = time.perf_counter()
        metric.attempts = attempts
        metric.success = True
        
        logger.info(
            f"Completed async task for '{string_name}' - "
            f"found {hash_string} in {duration}s ({attempts} attempts)"
        )
    except Exception as e:
        metric.end_time = time.perf_counter()
        metric.error_msg = str(e)
        logger.error(f"Async task for '{string_name}' failed: {e}")
    
    return metric

async def main() -> None:
    """Execute async hash finding with comprehensive metrics."""
    config = PipelineConfig.from_env()
    logger = setup_logging(config)
    collector = MetricsCollector()
    
    start_time = time.perf_counter()
    logger.info(f"Starting async execution for {len(config.crypto_targets)} targets")
    
    results: List[PipelineMetrics] = await asyncio.gather(
        *[async_task(crypto, config) for crypto in config.crypto_targets],
        return_exceptions=True
    )
    
    for result in results:
        if isinstance(result, PipelineMetrics):
            collector.add_metric(result)
    
    summary = collector.summary()
    total_duration = round(time.perf_counter() - start_time, 2)
    
    logger.info(
        f"Async execution completed in {total_duration}s - "
        f"Success: {summary.get('successful', 0)}/{summary.get('total_tasks', 0)}, "
        f"Avg Duration: {summary.get('avg_duration', 0)}s, "
        f"Success Rate: {summary.get('success_rate', 0)}%"
    )

if __name__ == '__main__':
    asyncio.run(main())