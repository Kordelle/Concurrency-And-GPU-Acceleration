import math
import random
import time
import logging
from typing import Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants for hash calculation and performance tuning
HASH_DIVISOR = 5000000000
MAX_ITERATIONS = 1000000  # Circuit breaker to prevent infinite loops

def time_to_find_hashed_string_value(string_name: str) -> Tuple[int, float, int, int]:
    """
    Find hash value through random guessing with dual attempts per iteration.
    
    Args:
        string_name: Input string to hash and find
        
    Returns:
        Tuple of (matched_value, duration_seconds, target_hash, attempts)
        
    Raises:
        RuntimeError: If max iterations exceeded without finding match
    """
    hash_string = abs(math.floor(hash(string_name) / HASH_DIVISOR))
    logger.info(f"Starting hash search for '{string_name}' with target: {hash_string}")
    
    duration = 0.0
    value = 0
    guess_1, guess_2 = 0, 0
    attempts = 0
    start_time = time.perf_counter()  # More precise than time.time()
    
    while guess_1 != hash_string and guess_2 != hash_string:
        if attempts >= MAX_ITERATIONS:
            raise RuntimeError(f"Max iterations ({MAX_ITERATIONS}) exceeded for '{string_name}'")
            
        guess_1 = random.randint(0, hash_string + 1)
        guess_2 = random.randint(0, hash_string + 1)
        
        if guess_1 == hash_string or guess_2 == hash_string:
            end_time = time.perf_counter()
            duration = round(end_time - start_time, 4)
            value = guess_1 if guess_1 == hash_string else guess_2
            logger.info(f"Match found for '{string_name}' after {attempts + 1} attempts in {duration}s")
            
        attempts += 1
        
    return value, duration, hash_string, attempts