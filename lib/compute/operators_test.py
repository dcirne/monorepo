import pytest
import sys

from compute import add, sub, mul, div

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))

def test_addition():
    r = add(2, 2)
    assert r == 4

    r = add(-1, -5)
    assert r == -6

    with pytest.raises(TypeError):
        r = add(7, "a")

def test_subtraction():
    r = sub(2, 2)
    assert r == 0

    r = sub(1, -5)
    assert r == 6

    with pytest.raises(TypeError):
        r = sub(7, "a")

def test_multiplication():
    r = mul(2, 8)
    assert r == 16

    r = mul(6, -7)
    assert r == -42

    with pytest.raises(TypeError):
        r = mul(7, "a")

def test_division():
    r = div(32, 4)
    assert r == 8

    r = div(6, -2)
    assert r == -3

    with pytest.raises(TypeError):
        r = div("a", 2)

    with pytest.raises(ValueError):
        r = div(6, 0)
