# 1. Generate a SyntaxError by printing a string without parentheses.
#print "Hello, world"

#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print("Hello, world")

# 2. Generate a NameError by trying to use an undefined variable.
#print(dinner)

#NameError: name 'dinner' is not defined

dinner = "fish"
print(dinner)

# 3. Generate an IndexError by accessing a non-existent index of a list.

my_shopping_list = ["tomatoes", "onions", "garlic", "milk", "eggs"]

#print(my_shopping_list[8])
#IndexError: list index out of range

print(my_shopping_list[-1])
print(my_shopping_list[2])

# 4. Generate a ModuleNotFoundError by importing a non-existent module.

#from markdown import postproCessors
#ModuleNotFoundError: No module named 'markdown'

from random import choice


# 5. Generate an AttributeError by accessing an attribute that does not exist.
import random

#print(random.Choices)

#AttributeError: module 'random' has no attribute 'Choices'. Did you mean: 'choices'?

print(random.choice)


# 6. Generate a KeyError by accessing a non-existent key in a dictionary.

dictionary = {"Color":"Green", "Animal":"Dog", "Plant":"Monstera"}

#print(dictionary["Name"])
#KeyError: 'Name'

print(dictionary.get("Name", "Not Found"))  # Access with default value

# 7. Generate a TypeError by using incorrect types (string index in a list).

dictionary = {"Color":"Green", "Animal":"Dog", "Plant":"Monstera"}

#print(dictionary("Color"))
#TypeError: 'dict' object is not callable

print(dictionary["Color"])

# 8. Generate an ImportError by importing a function that does not exist from a module.

#from random import Choices
#ImportError: cannot import name 'Choices' from 'random' (C:\Users\visha\AppData\Local\Programs\Python\Python312\Lib\random.py). Did you mean: 'choices'?

from random import choices

# 9. Generate a ValueError by trying to convert a non-numeric string to an integer.

#my_weight = int("55 kilos")
#print(my_weight)    ValueError: invalid literal for int() with base 10: '55 kilos'

my_weight = int("55")
print(my_weight)

# 10. Try to detect if an error occurs using try-except with a KeyError.

dictionary2 = {"Book":"The Lord of Rings", "Character":"Legolas"}

try:
    print(dictionary2["Favorite"])
except KeyError:
    print("Error: Not founded key")
