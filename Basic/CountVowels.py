# 4. Counting Vowels in a Given Word
def countVowels(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0

    inChar = []
    for char in word:
        if char in vowel:
            count +=1
            inChar.append(char)
    print(f"Given word {word} here Count is {count} and vowels is {inChar}")

countVowels(word = "programming")
countVowels("python")

'''
Given word programming here Count is 3 and vowels is ['o', 'a', 'i']
Given word python here Count is 1 and vowels is ['o']
'''