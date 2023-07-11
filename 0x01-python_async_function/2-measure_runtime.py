#!/usr/bin/env python3
"""measures and return the execution time for function wait_n"""

from time import perf_counter
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """ returns the execution time of wait_n"""
    begin = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    timeelapsed = perf_counter() - begin
    return timeelapsed / n

