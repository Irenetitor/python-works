# 1. Generate a list using comprehension with the numbers from 0 to 10.
my_list = list(range(11))
print(my_list)

# 2. Create a list using comprehension with the squares of the numbers from 1 to 10.
square_list = [i * i for i in range (1, 11)]
print(square_list)

# 3. Generate a list using comprehension with the even numbers from 0 to 20.
even_list = [i for i in range (21) if i % 2 == 0]
print(even_list)

# 4. Convert a list of temperatures from Celsius to Fahrenheit using comprehension.
celsius_list = [23, 12, 32, 31, 26, 15]
fahrenheit = [(c * 9/5) + 32 for c in celsius_list]
print(fahrenheit)

# 5. Create a list using comprehension with the characters of a string.
text = "Learning"
result = [chr for chr in text]
print(result)

# 6. Filter a list of words and keep only those that have more than 4 letters using comprehension.
words_list = ["table", "sofa", "chair", "tv", "fridge", "tap"]
valid = [i for i in words_list if len(i) > 4]
print(valid)

# 7. Increase each number in a list by 5 using comprehension and an external function.
plus_five = [i + 5 for i in my_list]
print(plus_five)


# 8. Create a list of booleans indicating whether each number is greater than 10 using comprehension.
list = [6, 13, 45, 9, 20, 4, 11, 0]
bigger_ten = [i > 10 for i in list]
print(bigger_ten)

# 9. Multiply only the odd numbers by 3 in a list using comprehension.
triple_odds = [n * 3 for n in my_list if n % 2 != 0]
print(triple_odds)

# 10. Use nested list comprehension to generate a 3x3 matrix with numbers from 1 to 9.
matrix_list = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix_list)