#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float."""

def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """defines a function which returns the sum of floats as a float"""
    return sum(mxd_lst)
