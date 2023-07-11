#!/usr/bin/env python3
''' This module returns a random number'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Takes in an integer with default value of 10, waits for a random delay
    between 0 and max_delay and eventually returns it.
    '''
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
