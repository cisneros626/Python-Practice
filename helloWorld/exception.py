# exception --> events detected during execution that interrupt the flow of  a program
try:
    numerator = int(input("Enter a number as numerator: "))
    denominator = int(input("Enter a number as denominator: "))
    result = numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print("You can not divide by zero")
    print(e)
except ValueError as e:
    print("Only enter numbers!!")
    print(e)
except Exception as e:
    print("Something went wrong :(")
    print(e)