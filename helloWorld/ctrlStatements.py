# break --> Terminate loop entirely
# continue --> Skips to the next iteration of the loop
# pass --> does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

even = []
for i in range(1,101):
    if i%2 == 0:
        pass
    else:
        even.append(i)
        # print(i, end=", ")
print(even)
print(len(even))