# 19. Building a Pyramid in Python
floors = 5
h = 2*floors-1
for i in range(1, floors*2, 2):
    print('{:^{}}'.format('*'*i, h))

# 20. Randomizing the Items of a List in Python
from random import shuffle
lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)
'''
    *    
   ***   
  *****
 *******
*********
['is', 'Python', 'Easy']
'''