#!/usr/bin/env python3
''' This module yields random number between 0 and 10 '''

import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    '''
    Yields a random number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
