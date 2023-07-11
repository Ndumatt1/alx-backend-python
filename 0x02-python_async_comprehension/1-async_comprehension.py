#!/usr/bin/env python3
''' This module collects 10 random numbers and return the 10 random numbers'''

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    COllects 10 random numbers using an async comprehension
    Returns the 10 random numbers
    '''
    results = [i async for i in async_generator()]
    return results
