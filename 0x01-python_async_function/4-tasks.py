#!/usr/bin/env python3
"""
Module that defines the task_wait_n function using asyncio tasks.
"""

import asyncio
from typing import List
from importlib import import_module

# Import task_wait_random from the 3-tasks.py module
task_wait_random = import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute mult. coroutines concurrently and return a list of delays.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
