import time
import asyncio
from guess_a_hash import time_to_find_hashed_string_value

"""
    Asynchronous Example of a function
        @param time_to_find_hashed_string_value: Function to find hashed string value
        @param string_name: Name of the string to find hashed value for
"""

async def async_task(string_name):
    start_time = time.time()
    print(f"Starting async task for '{string_name}'")
    await asyncio.to_thread(time_to_find_hashed_string_value, string_name)
    end_time = time.time()
    print(f"Finishing async task for '{string_name}' in {round(end_time - start_time, 2)} seconds")

async def main():
    await asyncio.gather(
        async_task('Bitcoin'),
        async_task('Ethereum'),
        async_task('Litecoin'),
        async_task('Dogecoin'),
        async_task('Cardano'),
        async_task('Polkadot')
    )

# Run the async main function
asyncio.run(main())
