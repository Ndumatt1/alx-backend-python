#!/usr/bin/env python3
''' Returns a function that multiplies a float by multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Takes a float multiplier as argument
    Returns a function that multiplies a float by multiplier
    '''
    def func(number: float) -> float:
        ''' Multiplies a float by multiplier'''
        return number * multiplier

    return func
