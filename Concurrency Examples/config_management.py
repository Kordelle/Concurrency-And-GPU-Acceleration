"""
Centralized configuration management.
Production pattern: Environment-based config for dev/staging/prod.
"""
import os
from dataclasses import dataclass
from typing import List

@dataclass
class PipelineConfig:
    """Configuration for concurrency pipeline execution."""
    
    # Processing targets
    crypto_targets: List[str] = None
    
    # Performance tuning
    hash_divisor: int = 5_000_000_000
    max_iterations: int = 1_000_000
    
    # Concurrency settings
    max_workers: int = None  # None = use CPU count
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    def __post_init__(self):
        if self.crypto_targets is None:
            self.crypto_targets = self._get_default_targets()
        if self.max_workers is None:
            self.max_workers = os.cpu_count() or 4
    
    @staticmethod
    def _get_default_targets() -> List[str]:
        return [
            'Bitcoin', 'Ethereum', 'Litecoin', 
            'Dogecoin', 'Cardano', 'Polkadot'
        ]
    
    @classmethod
    def from_env(cls) -> 'PipelineConfig':
        """Load configuration from environment variables."""
        return cls(
            crypto_targets=os.getenv('CRYPTO_TARGETS', '').split(',') or None,
            hash_divisor=int(os.getenv('HASH_DIVISOR', 5_000_000_000)),
            max_iterations=int(os.getenv('MAX_ITERATIONS', 1_000_000)),
            max_workers=int(os.getenv('MAX_WORKERS', 0)) or None,
            log_level=os.getenv('LOG_LEVEL', 'INFO')
        )