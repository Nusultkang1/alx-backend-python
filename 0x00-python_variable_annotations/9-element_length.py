#!/usr/bin/env python3
""" annotates the function's parameters and returns values with the appropriate types"""

def element_length(lst: list[str]) -> List[Tuple[str, int]]:
    """ defines the function element_length to return a list"""
    return [(i, len(i)) for i in lst]
