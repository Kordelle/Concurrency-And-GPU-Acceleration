# Concurrency and GPU Acceleration Examples

Python examples demonstrating different concurrency patterns and GPU acceleration techniques through practical hash computation and data processing benchmarks.

## Quick Start

```bash
cd "Concurrency Examples"
python threading.py      # I/O-bound concurrency
python multiprocess.py   # CPU-bound parallelism  
python asynchronous.py   # High-concurrency async
```

## Project Structure

```
Concurrency Examples/
├── threading.py         # Threading pattern with metrics
├── multiprocess.py      # Multiprocessing with Queue
├── asynchronous.py      # Async/await pattern
├── guess_a_hash.py      # Core computational workload
├── metrics.py           # Performance tracking
├── config.py            # Environment-based config
└── type_definitions.py  # Shared types/constants
```


## Concurrency Examples

Each example processes hash computations for cryptocurrency targets (Bitcoin, Ethereum, Litecoin, Dogecoin, Cardano, Polkadot) using different concurrency patterns.

- **Threading** - Multi-threaded execution for I/O-bound operations
- **Multiprocessing** - True parallelism across CPU cores, bypasses GIL
- **Async/Await** - Non-blocking I/O with event loop concurrency

All examples include structured logging, metrics collection, and environment-based configuration.

## GPU Acceleration

- **CPU Performance** - Pandas operations baseline via [`cpu_performance.py`](PandasBenchmarking/cpu_performance.py)
- **RAPIDS cuDF** - GPU-accelerated DataFrames via [`rapids_performance.py`](PandasBenchmarking/rapids_performance.py)

Demonstrates 10-100x speedup for large dataset operations using NVIDIA CUDA acceleration.

## Configuration

Override defaults via environment variables:

```bash
export CRYPTO_TARGETS="Bitcoin,Ethereum"
export MAX_ITERATIONS=500000
export LOG_LEVEL=DEBUG
python multiprocess.py
```

## Key Implementation Details

- **Hash Function**: Uses Python's built-in `hash()` function with mathematical transformation to create simulate deterministic targets
- **Performance Measurement**: All examples include timing mechanisms to measure execution duration
- **RAPIDS Integration**: GPU acceleration leverages `cudf.pandas.install()` for seamless pandas API compatibility

## Capabilities Overview

| Technique | Pros | Cons | Best Use Case |
|-----------|------|------|---------------|
| **Threading** | • Low memory overhead<br>• Easy to implement<br>• Good for I/O-bound tasks | • Limited by GIL<br>• No true CPU parallelism<br>• Race condition risks | Web scraping, file I/O, network requests |
| **Async/Await** | • Very efficient for I/O<br>• Single-threaded (no locks)<br>• Excellent scalability | • Learning curve<br>• CPU-bound tasks block<br>• Requires async libraries | HTTP APIs, database queries, concurrent downloads |
| **Multiprocessing** | • True parallelism<br>• Bypasses GIL<br>• Uses multiple CPU cores | • High memory usage<br>• Slow inter-process communication<br>• Complex data sharing | CPU-intensive calculations, data processing, image/video processing |
| **GPU Acceleration** | • Massive parallelism<br>• Fast for large datasets<br>• Hardware acceleration | • GPU memory limitations<br>• Setup complexity<br>• Not all operations supported | Large dataset operations, machine learning, scientific computing |