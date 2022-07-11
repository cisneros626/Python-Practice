# First we see positional arguments

def hello(name,middleName,lastName):
    print("Hello " + name, middleName, lastName)
    
x = hello("Alejandro", "Cisneros", "Perez")
y = hello("Perez", "Alejandro", "Cisneros")

# The order of the arguments does matter

# With Keyword arguments the position in which we declare our arguments does not matter

def helloTwo(name, middleName, lastName):
    print("Hello " + name, middleName, lastName)
    
k = helloTwo(middleName="Cisneros", lastName="Perez", name="Alejandro")