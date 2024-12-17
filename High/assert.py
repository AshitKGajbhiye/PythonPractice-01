'''Python assertions in any programming language are the debugging tools that help in the smooth flow of code.
We can say that assertion is the boolean expression that checks if the statement is True ot False. If the statement is true then it does nothing and continues the execution, but if the statement is False then it stops the execution of the program and throws on error.'''
a = 4
b = 0

assert b!=0, "Invalid Operation"
print(a/b)

'''
Traceback (most recent call last):
  File "e:\AshitOffice\AshitG-CT\practice-01\OOPs\assert.py", line 7, in <module>
    assert b!=0, "Invalid Operation"
           ^^^^
AssertionError: Invalid Operation'''