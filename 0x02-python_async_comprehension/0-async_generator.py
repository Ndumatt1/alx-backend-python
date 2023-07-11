#!/usr/bin/env python3
''' This module yields random number between 0 and 10 '''

import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, float]:
    '''
    Yields a random number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
