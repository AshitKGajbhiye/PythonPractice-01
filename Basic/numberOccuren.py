# https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md
# 6. Counting the Number of Occurances of a Character in a String
def CountOccurence(word, char):
    count = 0
    for occurence in word:
        if occurence == char:
            count +=1
    return count

print(CountOccurence("Programming", 'm'))
print(CountOccurence("Python", 'y'))