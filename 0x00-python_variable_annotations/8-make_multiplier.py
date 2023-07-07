#!/usr/bin/env python3
"""a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """defines a function make_multiplier to return a float"""

    def mul(v: float) -> float:
        """defines a function mul to return the product as a float"""
        return v * multiplier
    return mul
