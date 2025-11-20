import math
import random
import time

# Function to find all target values and time to reach it
def time_to_find_hashed_string_value(string_name: str) -> int:
    hash_string = abs(math.floor(hash(string_name) / 5000000000))
    duration = 0
    value = 0
    guess_1, guess_2 = 0, 0
    i = 0
    start_time = time.time()
    while guess_1 != hash_string and guess_2 != hash_string:
        guess_1 = random.randint(0, hash_string + 1)
        guess_2 = random.randint(0, hash_string + 1)
        #print(f"{round(start_time,2)} - Thread for '{string_name}' - Attempt #{i} - Guess 1: {guess_1} | Guess 2: {guess_2} | Target: {hash_string}")
        #print(f"Attempt #{i} - Guess 1: {guess_1} | Guess 2: {guess_2} | Target: {hash_string}")
        if guess_1 == hash_string or guess_2 == hash_string:
            end_time = time.time()
            elapsed_time = end_time - start_time
            duration = round(elapsed_time, 2)
            value = guess_1 if guess_1 == hash_string else guess_2
        i += 1
    return value, duration, hash_string, i



