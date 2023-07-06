#!/usr/bin/python3

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mul(v: float) -> float:
        return v * multiplier
    return mul
