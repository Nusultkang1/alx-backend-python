#!/usr/bin/env python3
"""asynchronous function that takes two arguments and returns a random delay"""

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """returns wait_random n number of times"""
    tasks = []
    delays = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]

