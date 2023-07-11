#!/usr/bin/python3
"""Asynchronous coroutine that returns a random delay value from 0 to max_delay"""

import random
import asyncio

async def wait_random(max_delay=10):
    """returns a random delay value between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
