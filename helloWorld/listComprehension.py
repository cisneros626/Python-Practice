# list comprehension --> A way to create a new list with less syntax.
#                        can mimic certain lambda functions, easier to read
# 
# list = [return element for item in iterable if z<s]

squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

squaresTwo = [i*i for i in range(1,11)]
print(squaresTwo)

even_list = [i for i in range(1,101) if i%2 == 0]
odd_list = [i for i in range(1,101) if i%2 == 1]

print("Even List:\n", even_list)
print("\nOdd List:\n", odd_list)