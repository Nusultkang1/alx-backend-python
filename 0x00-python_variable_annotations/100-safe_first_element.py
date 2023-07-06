#!/usr/bin/env python3

def safe_first_element(lst: Union[list, tuple]) -> Any:
    if lst:
        return lst[0]
    else:
        return None

