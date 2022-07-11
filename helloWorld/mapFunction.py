# map() --> applies a function to each item in an iterable

# map(function, iterable)

j =[1,2,3,4,5,6,7,8,9,10]

even_square = lambda x: x**2 if x%2 == 0 else x
odd_square = lambda x: x**2 if x%2 == 1 else x

even_square_map = list(map(even_square,j))
print("List with even numbers squared: \n", even_square_map)

odd_square_map = list(map(odd_square,j))
print("\nList with odd numbers squared: \n", odd_square_map)