#!/usr/bin/python3

def element_length(lst: list[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
