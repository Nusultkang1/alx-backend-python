#!/usr/bin/env python3
""" a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple."""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """define a function to_kv and returns a tuple"""
    return k, float(v ** 2)

