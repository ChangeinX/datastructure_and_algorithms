"""
This module is part of a series of modules that studies data structures and algorithms.
This module contains the implementation of the binary search algorithm.
"""
import logging
import time
from typing import List, Any

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('binary_search.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def binary_search(data: List[Any], target: Any) -> int:
    """
    This function implements the binary search algorithm. It takes a list of data and a target value and returns the index
    of the target value in the list if it is found. If the target value is not found, the function returns -1. Time
    is captured and logged.
    """
    logger.debug(f'Beginning binary search of prime numbers of length {len(data)} for {target}.')
    start_time = time.time()
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            logger.debug(f'Found {target} at index {mid}.')
            logger.debug(f'Binary search took {time.time() - start_time} seconds.')
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    logger.debug(f'{target} not found.')
    return -1


# list of data comes from primes1.txt and is stored in a list
# Convert text file to list
with open('primes1.txt', 'r') as f:
    data = f.read().split()
    data = [int(x) for x in data]

# Sample target value
target = 15346759

# Call the binary search function
index = binary_search(data, target)

# Print the result
print(f'Index of {target} is {index}.')