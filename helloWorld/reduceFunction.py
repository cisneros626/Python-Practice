# reduce() --> apply a function to an iterable and reduce it to a single cumulative value.
#               performs function on first two elements and repeats process until one value remains.

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y: x+y, letters)
print(word)

# for i in letters:
#     print(i, end="")
    
    