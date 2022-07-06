"""
This program builds an m*n square with a symbol of choice
"""
    
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print(symbol)