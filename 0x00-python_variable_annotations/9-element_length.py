#!/usr/bin/env python3
''' This module returns an iterable'''

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns an iterable'''
    return [(i, len(i)) for i in lst]
