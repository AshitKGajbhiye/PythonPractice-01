def days(index):
    day = ['S','M','T','W','Tr','F','St']            
    yield day[index]    
    yield day[index+1]  
  
res = days(0)
print(next(res), next(res))

days = ['S','M','M','M','F','S']
y = set(days)

print([[x,days.count(x)] for x in y])

# > [['M', 3], ['S', 2], ['F', 1]]