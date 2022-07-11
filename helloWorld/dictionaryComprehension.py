# dictionary comprehension --> Create dictionaries using an expression.
#                               can replace for loops and certain lambda functions
# 
# dictionary = {key: expression for(key, value) in iterable}

cities_in_F = {"Monterrey": 32, "Saltillo": 58, "Torreon": 45, "Apodaca": 64}

cities_in_C = {key: round((value-32)*(5/9), 2) for(key, value) in cities_in_F.items()}

print(cities_in_C)