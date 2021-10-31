def compare_anagrams(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)
