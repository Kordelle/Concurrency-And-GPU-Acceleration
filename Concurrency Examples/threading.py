import threading
import logging
from typing import List
from guess_a_hash import time_to_find_hashed_string_value

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration for crypto currencies to process
CRYPTO_TARGETS = ['Bitcoin', 'Ethereum', 'Litecoin', 'Dogecoin', 'Cardano', 'Polkadot']

def task(string_name: str) -> None:
    """
    Execute hash finding task and log results.
    
    Args:
        string_name: Name of cryptocurrency to process
    """
    try:
        value, duration, hash_string, attempts = time_to_find_hashed_string_value(string_name)
        logger.info(
            f"Thread for '{string_name}' found target {hash_string} "
            f"of value {value} in {duration}s after {attempts} attempts"
        )
    except Exception as e:
        logger.error(f"Thread for '{string_name}' failed: {e}")

def main() -> None:
    """Execute threaded hash finding for multiple targets."""
    threads: List[threading.Thread] = []
    
    # Create and start threads
    for crypto in CRYPTO_TARGETS:
        thread = threading.Thread(
            target=task,
            args=(crypto,),
            name=f"Thread-{crypto}"
        )
        thread.start()
        threads.append(thread)
    
    # Wait for completion
    for thread in threads:
        thread.join()
    
    logger.info("All threads completed successfully")

if __name__ == '__main__':
    main()