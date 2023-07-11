#!/usr/bin/python3
"""asynchronous function that takes two arguments and returns a random delay"""

import asyncio
import random
from 0-basic_async_syntax.py import wait_random

async def wait_n(n, max_delay):
    """returns wait_random n number of times"""
    tasks = []
    delays = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
