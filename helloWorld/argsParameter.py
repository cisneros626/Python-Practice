# *args --> parameter that will pack all arguments into a tuple  useful so that a function  can accept
#           a varying amount of arguments

"""def sum(a,b):
    return a+b

print(sum(1,2,3))

Traceback (most recent call last):
  File "c:\DataScience\Python-Practice\helloWorld\argsParameter.py", line 7, in <module>
    print(sum(1,2,3))
TypeError: sum() takes 2 positional arguments but 3 were given"""

def sum(*args):
    sum = 0
    for i in args:
        # sum = sum +i
        sum += i
    return sum

print(sum(1,2,3))