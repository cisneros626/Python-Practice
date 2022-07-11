# High Order Function --> Function that either:
#                           1. Accepts a function as an argument
#                           2. Returns a function
# IN PYTHON FUNCTIONS ARE ALSO TREATED AS OBJECTS

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello World")
#     print(text)
    
# hello(loud)
# hello(quiet)

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def calc(a, b, func):
    return a, b, func(a,b)


result = calc(8, 3, sum)
print('{} + {} = {}'.format(result[0],result[1],result[2]))

result = calc(8, 3, sub)
print('{} - {} = {}'.format(result[0],result[1],result[2]))

result = calc(8, 3, mult)
print('{} * {} = {}'.format(result[0],result[1],result[2]))

result = calc(8, 3, div)
print('{} / {} = {}'.format(result[0],result[1],result[2]))