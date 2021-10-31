from utils import compare_anagrams

if __name__ == "__main__":
    list1 = ["car", "race"]
    list2 = ["arc", "pace"]

    for str1, str2 in zip(list1, list2):
        if compare_anagrams(str1, str2):
            print(f"{str1} and {str2} are anagrams")
        else:
            print(f"{str1} and {str2} are not anagrams")
