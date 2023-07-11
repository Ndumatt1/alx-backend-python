#!/usr/bin/env python3
''' This module returns list of all delays'''

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    '''
    Returns the list of all the delays
    The list of the delays sorted in ascending order
    '''
    delay_list = []
    for _ in range(0, n):
        rand_value = task_wait_random(max_delay)
        rands = await rand_value
        delay_list.append(rands)
    return delay_list
