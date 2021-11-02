import pytest
import sys

from utils import compare_anagrams

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))

def test_compare_anagrams():
    result = compare_anagrams("Night", "Thing")
    assert result

    result = compare_anagrams("race", "pace")
    assert not result

    with pytest.raises(TypeError):
        result = compare_anagrams(1, "car")

    with pytest.raises(TypeError):
        result = compare_anagrams("arc", 2)
