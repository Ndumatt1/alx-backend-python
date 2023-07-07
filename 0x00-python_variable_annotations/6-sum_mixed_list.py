#!/usr/bin/env python3
''' This module returns the sum of values in a list'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Takes a list of integers and floats and return the sum as a float
    '''
    sum: float = 0

    for num in range(len(mxd_lst)):
        sum += mxd_lst[num]
    return sum
