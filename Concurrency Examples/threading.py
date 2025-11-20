import threading
from guess_a_hash import time_to_find_hashed_string_value

"""
    Threading Example of a function
        @param time_to_find_hashed_string_value: Function to find hashed string value
        @param string_name: Name of the string to find hashed value for
"""

def task(time_to_find_hashed_string_value, string_name):
    value, duration, hash_string, attempts = time_to_find_hashed_string_value(string_name)
    print(f"Thread for '{string_name}' found target {hash_string} of value {value} in {duration} seconds after {attempts} attempts")

# Create threads for concurrent execution
thread1 = threading.Thread(target=task, args=(time_to_find_hashed_string_value, 'Bitcoin'))
thread2 = threading.Thread(target=task, args=(time_to_find_hashed_string_value, 'Ethereum'))
thread3 = threading.Thread(target=task, args=(time_to_find_hashed_string_value, 'Litecoin'))
thread4 = threading.Thread(target=task, args=(time_to_find_hashed_string_value, 'Dogecoin'))
thread5 = threading.Thread(target=task, args=(time_to_find_hashed_string_value, 'Cardano'))
thread6 = threading.Thread(target=task, args=(time_to_find_hashed_string_value, 'Polkadot'))

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()