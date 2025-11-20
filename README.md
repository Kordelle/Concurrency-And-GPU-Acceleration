# Concurrency and GPU Acceleration Examples

Python examples demonstrating different concurrency patterns and GPU acceleration techniques through practical hash computation and data processing benchmarks.

## Concurrency Examples
- **Threading** - Multi-threaded execution for I/O-bound operations using cryptocurrency hash finding
- **Async/Await** - Asynchronous programming patterns with asyncio framework for concurrent task execution
- **Multiprocessing** - CPU-bound parallel processing across multiple cores with true parallelism

Each concurrency example uses the [`guess_a_hash.py`](Concurrency%20Examples/guess_a_hash.py) function to simulate computational workload by finding target hash values for different cryptocurrency names (Bitcoin, Ethereum, Litecoin, Dogecoin, Cardano, Polkadot).

## GPU Acceleration
- **CPU Performance** - Standard pandas operations baseline benchmarking using [`cpu_performance.py`](PandasBenchmarking/cpu_performance.py)
- **RAPIDS cuDF** - GPU-accelerated DataFrame operations with CUDA integration via [`rapids_performance.py`](PandasBenchmarking/rapids_performance.py)

**TODO:** Multiprocessed CRUD operations in a pd.Dataframe for managing prior computational hash guesses

The GPU acceleration examples compare traditional CPU-based pandas operations against RAPIDS cuDF for large dataset processing, demonstrating the performance gains achievable through GPU acceleration.

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