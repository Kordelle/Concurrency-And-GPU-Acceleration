"""
Concurrency patterns for high-throughput data pipelines.
Demonstrates threading, multiprocessing, and async patterns for NVIDIA-scale workloads.
"""
from .guess_a_hash import time_to_find_hashed_string_value
from .metrics import PipelineMetrics, MetricsCollector
from .config import PipelineConfig
from .type_definitions import HashResult, CryptoList, DEFAULT_CRYPTO_TARGETS

__all__ = [
    'time_to_find_hashed_string_value',
    'PipelineMetrics',
    'MetricsCollector',
    'PipelineConfig',
    'HashResult',
    'CryptoList',
    'DEFAULT_CRYPTO_TARGETS'
]

__version__ = '1.0.0'