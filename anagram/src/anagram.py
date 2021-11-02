from termcolor import colored
from utils import compare_anagrams

if __name__ == "__main__":
    list1 = ["car", "race", "State", "Elbow"]
    list2 = ["arc", "pace", "Taste", "Desserts"]

    for str1, str2 in zip(list1, list2):
        if compare_anagrams(str1, str2):
            text_color = "cyan"
            result_message = "are anagrams"
        else:
            text_color = "red"
            result_message = "are not anagrams"


        str1 = colored(str1, text_color)
        str2 = colored(str2, text_color)
        print(f"{str1} and {str2} {result_message}")
