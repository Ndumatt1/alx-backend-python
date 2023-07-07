#!/usr/bin/env python3
''' This module takes a string and floast/int
and return the square of the float or int as an int
'''

from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Returns tuple with the first argument as a string
    and the second argument a float
    '''

    return (k, v * v)
