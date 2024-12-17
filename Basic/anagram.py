# 13. Comparing Two Strings for Anagrams
def anagram(str1, str2):
    str1 = list(str1.upper())
    str2 = list(str2.upper())

    str1.sort(), str2.sort()
    if str1 == str2:
        print("TRUE")
    else:
        print("FALSE")

str1 = "Listen"
str2 = "Silent"
anagram(str1, str2)