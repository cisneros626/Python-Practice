# 2D list --> a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hambuger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

# print(food)
p = 0
for i in food:
    for j in drinks:
        print(j)
        p += 1
    if p == len(drinks):
        break