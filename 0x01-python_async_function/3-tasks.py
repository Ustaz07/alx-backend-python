#!/usr/bin/env python3
"""
Module for creating asyncio tasks from the wait_random coroutine.
"""

import asyncio
from _basic_async_syntax import wait_random  # Change this to: from 0_basic_async_syntax import wait_random if file name is 0-basic_async_syntax.py

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that runs the wait_random coroutine with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio Task running the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
