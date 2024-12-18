# Lecture : Lambdas in Python.


def square(x):
    return x**2
 
print(square(9))


result = (lambda x: x**2)(7)
print(result)


result = (lambda x,y: x+y)(2,3)
print(result)


result = (lambda x,y: x+y)(y=2,x=3)
 
print(result)


result = (lambda x=20,y=10: x+y)(y=2)
print(result)


Lecture : Map


# Create a list of numbers
numbers = [1,2,3,4,5]
 
# a function to calculate the square of a number
def square(x):
    return x*x
 
for number in numbers:
    print(square(number))


numbers = [1,2,3,4,5]
 
def square(x):
    return x*x
 
 
new_list = list(map(square,numbers))
print(new_list)


# Lecture : Using map in different ways


numbers = ["1","2","3","4","5"]
print(numbers)
new_list = list(map(int,numbers))
print(new_list)


prices =[100,200,300,400,500]
 
new_prices = list(map(lambda x: x - x*5/100,prices))
print(new_prices)


names = ['john','rob','mike']
# capitalize first letter of every name
cap_names = list(map(str.capitalize,names))
print(cap_names)
# capitalize ever letter of the name
all_caps_names = list(map(str.upper,names))
print(all_caps_names)


Lecture : Filter in python.


nums = [1,2,3,4,5,6,7,8,9,10]
odd_nums=[]
for num in nums:
    if num%2==1:
        odd_nums.append(num)
print(odd_nums)


nums = [1,2,3,4,5,6,7,8,9,10]
 
def odd(x):
    if x%2==1:
        return x
odd_nums = list(filter(odd,nums))
print(odd_nums)


nums = [1,2,3,4,5,6,7,8,9,10]
 
odd_nums = list(filter(lambda x:x%2==1,nums))
print(odd_nums)


Lecture : Generators


def function():
    
 
    counter = 0
    while counter<=10:
       
        counter+=1
 
 
print(function())
 
print(list(function()))


def even_generator(x):
    for i in range(x):
        if i%2==0:
            yield i
 
print(list(even_generator(10)))