# https://www.geeksforgeeks.org/regular-expression-python-examples/
# 15. Counting the White Spaces in a String
string = "P r ogr am m in g "
print(string.count(' '))

# 16. Counting Digits, Letters, and Spaces in a String
import re
def getcount(name):
    digitCount = re.sub("[^0-9]", "", name)
    letterCount = re.sub("[^a-zA-Z]", "", name)
    spaceCount = re.findall("[ \n]", name)
    print("digitCount: ", digitCount)
    print("letterCount: ", letterCount)
    print("SpaceCount: ", spaceCount)

getcount('Python is 1')

# 17. Counting Special Characters in a String
specialchar = "!@#$%^&*()"
count = re.sub('[\w]+','',specialchar)
print(f"length of special characters: {len(count)}")

# 18. Removing All Whitespace in a String
string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", string)
print(result)
'''
7
digitCount:  1
letterCount:  Pythonis
SpaceCount:  [' ', ' ']
length of special characters: 10
CODE
'''