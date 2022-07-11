# filter() --> creates a collection of elements from an iterable for which a function returns true
# 
# filter(function, iterable)

# j = [("Mr. Alejandro", 48),
#      ("Ms. Esther", 45),
#      ("Ana", 24),
#      ("Alejandro Jr.", 22),
#      ("Santiago", 17),
#      ("Natalia", 13)]

# age = lambda data: data[1] >= 18

# adult = list(filter(age, j))

# print("The adults are: ")
# for i in adult:
#     print(i)
    
j = [1,2,3,4,5,6,7,8,9,10]

even = lambda e: e if e%2 == 0 else ""
odd = lambda e: e if e%2 == 1 else ""

even_list = list(filter(even, j))
print("The list with even numbers is:\n", even_list)

odd_list = list(filter(odd, j))
print("\nThe list with odd numbers is:\n", odd_list)