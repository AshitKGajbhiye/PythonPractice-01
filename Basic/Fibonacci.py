# https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md#7-writing-fibonacci-series
# 7. Writing Fibonacci Series
def fibonacci(n):
    fib = [0,1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    # Converting the list of integers to string
    print(', '.join(str(e) for e in fib))
    
fibonacci(5)
