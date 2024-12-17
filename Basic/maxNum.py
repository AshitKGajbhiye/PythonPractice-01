# 8. Finding the Maximum Number in a List
def maxNum(num):
    maxnumber = num[0]
    for n in num:
        if n > maxnumber:
            maxnumber = n
    print("maximum number: ", maxnumber)

maxNum([23, 45, 67, 124, 5, 57])

def minNumber(n):
    minNum = n[0]
    for min in n:
        if minNum > min:
            minNum = min
    print("Minimum number: ", minNum)

minNumber([23, 45, 67, 124, 5, 57])