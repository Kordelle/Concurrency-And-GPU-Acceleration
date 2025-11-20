import multiprocessing
from guess_a_hash import time_to_find_hashed_string_value

"""
    Multiprocessing Example of a function
        @param time_to_find_hashed_string_value: Function to find hashed string value
        @param string_name: Name of the string to find hashed value for
"""

# Multiprocessing Example of function

def cpu_bound_task(string_name):
    print(f"Process for '{string_name}' started")
    value, duration, hash_string, i = time_to_find_hashed_string_value(string_name)
    print(f"Process for '{string_name}' found target {hash_string} of value {value} in {duration} seconds after {i} attempts")

if __name__ == '__main__':
    # Create processes for parallel execution
    process1 = multiprocessing.Process(target=cpu_bound_task, args=('Bitcoin',))
    process2 = multiprocessing.Process(target=cpu_bound_task, args=('Ethereum',))
    process3 = multiprocessing.Process(target=cpu_bound_task, args=('Litecoin',))
    process4 = multiprocessing.Process(target=cpu_bound_task, args=('Dogecoin',))
    process5 = multiprocessing.Process(target=cpu_bound_task, args=('Cardano',))
    process6 = multiprocessing.Process(target=cpu_bound_task, args=('Polkadot',))

    # Start the processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()


    # Wait for all processes to complete if not joined than main program may end before they complete
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()

    print("All processes completed.")