"""
Common type definitions and constants for concurrency examples.
"""
from typing import Tuple, List

# Type aliases for clarity
HashResult = Tuple[int, float, int, int]  # (value, duration, hash_target, attempts)
CryptoList = List[str]

# Shared constants
DEFAULT_CRYPTO_TARGETS: CryptoList = [
    'Bitcoin',
    'Ethereum',
    'Litecoin',
    'Dogecoin',
    'Cardano',
    'Polkadot'
]

# Performance tuning constants
HASH_DIVISOR = 5000000000
MAX_ITERATIONS = 1000000