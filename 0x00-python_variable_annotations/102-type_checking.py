#!/usr/bin/env python3
''' This module returns a tuple'''

from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' Return a tuple'''
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
