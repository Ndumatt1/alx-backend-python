#!/usr/bin/env python3
''' This module returns the total runtime '''

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Execute async_comprehension four times in parallel using async.gather
    Return the total runtime
    '''
    start = time.perf_counter()
    result = await asyncio.gather(async_comprehension(), async_comprehension(),
                                  async_comprehension(), async_comprehension())
    end = time.perf_counter() - start
    return end
