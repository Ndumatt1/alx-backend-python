#!/usr/bin/env python3
''' This module returns a sum of list elements'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Returns the sum of a list
    '''
    sum: float = 0

    for num in range(len(input_list)):
        sum += input_list[num]
    return sum
