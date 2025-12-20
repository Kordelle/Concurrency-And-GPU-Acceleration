import time
import asyncio
import logging
from typing import Tuple
from guess_a_hash import time_to_find_hashed_string_value

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
CRYPTO_TARGETS = ['Bitcoin', 'Ethereum', 'Litecoin', 'Dogecoin', 'Cardano', 'Polkadot']

async def async_task(string_name: str) -> Tuple[str, float]:
    """
    Execute hash finding asynchronously using thread pool.
    
    Args:
        string_name: Name of cryptocurrency to process
        
    Returns:
        Tuple of (crypto_name, execution_time)
    """
    start_time = time.perf_counter()
    logger.info(f"Starting async task for '{string_name}'")
    
    try:
        value, duration, hash_string, attempts = await asyncio.to_thread(
            time_to_find_hashed_string_value,
            string_name
        )
        total_time = round(time.perf_counter() - start_time, 4)
        logger.info(
            f"Completed async task for '{string_name}' - "
            f"found {hash_string} in {duration}s ({attempts} attempts)"
        )
        return string_name, total_time
    except Exception as e:
        logger.error(f"Async task for '{string_name}' failed: {e}")
        return string_name, -1.0

async def main() -> None:
    """Execute async hash finding for all targets concurrently."""
    start_time = time.perf_counter()
    logger.info(f"Starting async execution for {len(CRYPTO_TARGETS)} targets")
    
    results = await asyncio.gather(
        *[async_task(crypto) for crypto in CRYPTO_TARGETS],
        return_exceptions=True
    )
    
    total_duration = round(time.perf_counter() - start_time, 2)
    successful = sum(1 for _, duration in results if duration > 0)
    
    logger.info(
        f"Async execution completed in {total_duration}s "
        f"({successful}/{len(CRYPTO_TARGETS)} successful)"
    )

if __name__ == '__main__':
    asyncio.run(main())