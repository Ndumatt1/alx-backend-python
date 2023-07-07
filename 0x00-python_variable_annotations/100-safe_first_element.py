#!/usr/bin/env python3
''' This module Returns the first element of a list or none'''


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Returns the first element of the list or None
    '''
    if lst:
        return lst[0]
    else:
        return None
