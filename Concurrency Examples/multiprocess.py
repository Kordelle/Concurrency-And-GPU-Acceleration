import multiprocessing
import time
import logging
from typing import List
from guess_a_hash import time_to_find_hashed_string_value

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
CRYPTO_TARGETS = ['Bitcoin', 'Ethereum', 'Litecoin', 'Dogecoin', 'Cardano', 'Polkadot']
CPU_COUNT = multiprocessing.cpu_count()

def cpu_bound_task(string_name: str) -> None:
    """
    Execute CPU-intensive hash finding in separate process.
    
    Args:
        string_name: Name of cryptocurrency to process
    """
    process_name = multiprocessing.current_process().name
    logger.info(f"Process {process_name} for '{string_name}' started")
    
    try:
        value, duration, hash_string, attempts = time_to_find_hashed_string_value(string_name)
        logger.info(
            f"Process {process_name} for '{string_name}' found target {hash_string} "
            f"of value {value} in {duration}s after {attempts} attempts"
        )
    except Exception as e:
        logger.error(f"Process {process_name} for '{string_name}' failed: {e}")

def main() -> None:
    """Execute parallel hash finding across multiple processes."""
    start_time = time.perf_counter()
    logger.info(f"Starting multiprocessing with {CPU_COUNT} CPU cores available")
    
    processes: List[multiprocessing.Process] = []
    
    # Create and start processes
    for crypto in CRYPTO_TARGETS:
        process = multiprocessing.Process(
            target=cpu_bound_task,
            args=(crypto,),
            name=f"Process-{crypto}"
        )
        process.start()
        processes.append(process)
    
    # Wait for completion
    for process in processes:
        process.join()
    
    total_duration = round(time.perf_counter() - start_time, 2)
    logger.info(f"All processes completed in {total_duration}s")

if __name__ == '__main__':
    main()