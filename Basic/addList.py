# 12. Adding Two List Elements Together
def addingList(lst1, lst2):
    result_list = []
    print ("Original list 1 : " + str(lst1))
    print ("Original list 2 : " + str(lst2))
    for i in range(0, len(lst1)):
        result_list.append(lst1[i] + lst2[i])
    print("Result : ", str(result_list))

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
addingList(lst1, lst2)
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]
addingList(test_list1, test_list2)
'''
Result :  [5, 7, 9]
'''

''' The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.'''
names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]

res = zip(names, scores)
print(list(res))
# [('John', 85), ('Alice', 90), ('Bob', 78), ('Lucy', 92)]

a = [1, 2, 3]
b = ['a', 'b', 'c']

res = zip()
print(list(res))    # []
res = zip(a)
print(list(res))    # [(1,),(2,),(3,)]
res = zip(a,b)
print(list(res))    # [(1, 'a'), (2, 'b'), (3, 'c')]