#!/usr/bin/python3

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, float(v ** 2)

