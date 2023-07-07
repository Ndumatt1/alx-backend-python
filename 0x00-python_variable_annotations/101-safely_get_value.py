#!/usr/bin/env python3
''' Adds annotations to the function'''

from typing import Mapping, TypeVar, Union, Any

T = TypeVar('T')


def safely_get_value(
     dct: Mapping[Any, T], key: Any, default: Union[T, None]) -> Union[Any, T]:
    '''
    Annotatate parameter and return values
    '''
    if key in dct:
        return dct[key]
    else:
        return default
