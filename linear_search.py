"""
This module is part of a series of modules that studies data structures and algorithms.
This module contains the implementation of the linear search algorithm.
"""
import logging
import time
from typing import List, Any

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('linear_search.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def linear_search(data: List[Any], target: Any) -> int:
    """
    This function implements the linear search algorithm. It takes a list of data and a target value and returns the index
    of the target value in the list if it is found. If the target value is not found, the function returns -1. Time
    is captured and logged.
    """
    logger.debug(f'Beginning linear search of prime numbers of length {len(data)} for {target}.')
    start_time = time.time()
    for index, value in enumerate(data):
        if value == target:
            logger.debug(f'Found {target} at index {index}.')
            logger.debug(f'Linear search took {time.time() - start_time} seconds.')
            return index
    logger.debug(f'{target} not found.')
    return -1


# list of data comes from primes.txt and is stored in a list

# Convert text file to list
with open('primes1.txt', 'r') as f:
    data = f.read().split()
    data = [int(x) for x in data]

# Sample target value
target = 15346759

# Call the linear search function
index = linear_search(data, target)

# Print the result
print(f'Index of {target} is {index}.')