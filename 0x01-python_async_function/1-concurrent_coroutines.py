#!/usr/bin/env python3
''' This module returns list of all delays'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Returns the list of all the delays
    The list of the delays sorted in ascending order
    '''
    delay_list = []
    count = 0
    while count < n:
        rand_value = await wait_random(max_delay)
        delay_list.append(rand_value)
        count += 1
    return delay_list
