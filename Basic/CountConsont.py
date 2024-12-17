# https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md
# 5. Counting Consonants in a Given Word
def countConsonents(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    cosonent_list = []

    for char in word:
        if char not in vowels:
            cosonent_list.append(char)
            count +=1

    print(f"Given word {word} count of consonents is {count} and list {cosonent_list}")

countConsonents("Programming")
countConsonents("python")

'''output
Given word Programming count of consonents is 8 and list ['P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
Given word python count of consonents is 5 and list ['p', 'y', 't', 'h', 'n']
'''