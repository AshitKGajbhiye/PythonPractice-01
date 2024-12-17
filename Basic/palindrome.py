# 14. Checking for Palindrome Using Extended Slicing Technique
str1 = "nitin"
def palindrome(str1):
    if str1 == str1[::-1]:
        print("Yes, Palindrome")
    else:
        print("No, Palindrome")

palindrome(str1)
palindrome("liril")

