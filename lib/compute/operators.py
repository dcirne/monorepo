def add(p1, p2):
    if not _is_number(p1) or not _is_number(p2):
        raise TypeError("At least one parameter is not a number")

    return p1 + p2

def sub(p1, p2):
    if not _is_number(p1) or not _is_number(p2):
        raise TypeError("At least one parameter is not a number")

    return p1 - p2

def mul(p1, p2):
    if not _is_number(p1) or not _is_number(p2):
        raise TypeError("At least one parameter is not a number")

    return p1 * p2

def div(p1, p2):
    if not _is_number(p1) or not _is_number(p2):
        raise TypeError("At least one parameter is not a number")

    if p2 == 0:
        raise ValueError("p2 cannot be zero")

    return p1 / p2

def _is_number(n) -> bool:
    return type(n) == int or type(n) == float
