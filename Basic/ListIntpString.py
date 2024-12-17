# 11. Converting a List into a String
def listIntoString(lst):
    string = ''.join(str(c) for c in lst)
    print(f"string: {string} and type: {type(string)}")
    
lst = ["P", "Y", "T", "H", "O", "N"]
listIntoString(lst)
lst2 = [1, 3, 45, 67, 5454]
listIntoString(lst2)

'''
string: PYTHON and type: <class 'str'>
string: 1345675454 and type: <class 'str'>
'''