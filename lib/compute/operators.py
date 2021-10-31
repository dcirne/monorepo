from lazy_object_proxy import Proxy
from typing import List

def add(p1, p2):
    valid_params = Proxy(_is_number([p1, p2]))
    valid_params

    return p1 + p2

def sub(p1, p2):
    valid_params = Proxy(_is_number([p1, p2]))
    valid_params

    return p1 - p2

def mul(p1, p2):
    valid_params = Proxy(_is_number([p1, p2]))
    valid_params

    return p1 * p2

def div(p1, p2):
    valid_params = Proxy(_is_number([p1, p2]))
    valid_params

    if p2 == 0:
        raise ValueError("p2 cannot be zero")

    return p1 / p2

def _is_number(numbers: List):
    for n in numbers:
        if type(n) != int and type(n) != float:
            raise TypeError("At least one parameter is not a number")
