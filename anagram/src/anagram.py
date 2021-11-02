from termcolor import cprint
from utils import compare_anagrams

if __name__ == "__main__":
    list1 = ["car", "race", "State", "Elbow"]
    list2 = ["arc", "pace", "Taste", "Desserts"]

    for str1, str2 in zip(list1, list2):
        if compare_anagrams(str1, str2):
            cprint(f"{str1} and {str2} are anagrams", "cyan")
        else:
            cprint(f"{str1} and {str2} are not anagrams", "red")
