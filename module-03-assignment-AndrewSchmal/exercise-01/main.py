# Write a Python decorator function that accepts any function as input, starts a timer, calls the function with a single argument, and 
# then ends the timer and prints out how long the function took to run. Use the Python time moduleLinks to an external site. to time the 
# accepted function. Decorate the long_running_task function using the Python decorator syntax and print the results.

import time
import functools

def timer(func):
    """Prints the runtime of the decorated function."""

    @functools.wraps(func)  # Preserve the decorated function's metadata
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # High-precision counter
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} seconds")
        return result

    return wrapper_timer

@timer  # Apply the decorator to the long_running_task function
def long_running_task(n):
    num = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                num += x + y + z
    return num


print(long_running_task(500))  # Call the decorated function

# I used w3schools and brocode youtube videos for this
# Short explanation:
# code defines a 'timer' decorator that measures and prints the runtime of a decorated function.
# It uses the high-precision counter from 'time.perf_counter()' to record start and end times.
# The 'functools.wraps' decorator preserves the original function's metadata.
# The 'long_running_task' function, when decorated with '@timer', showcases its execution time.
# It imports the time function to be able to track time