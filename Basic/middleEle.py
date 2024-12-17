# 10. Finding the Middle Element in a List
def middleElement(numList):
    middle= int(len(numList)/2)
    print("Middle: ", middle)
    print([numList[middle]])

numList = [1, 2, 3, 4, 5]
middleElement(numList)

'''
Middle:  2
3
'''