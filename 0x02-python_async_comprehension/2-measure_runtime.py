#!/usr/bin/env python3

""" Measure Runtime for Four Parallel Comprehensions """

from asyncio import gather
from time import time

# Import async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime for exe. async_comprehension 4 times in parallel."""
    start = time()

    # Create a list of tasks to run async_comprehension four times
    tasks = [async_comprehension() for _ in range(4)]

    # Run the tasks in parallel and wait for all to complete
    await gather(*tasks)

    end = time()

    return end - start
