def compare_anagrams(str1: str, str2: str) -> str:
    if type(str1) != str or type(str2) != str:
        raise TypeError("At least one parameter is not a string")

    if len(str1) != len(str2):
        return False

    return sorted(str1.lower()) == sorted(str2.lower())
