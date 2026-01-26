# 1. Create a lambda that adds two numbers.
addition = lambda firstnum, secondnum: firstnum + secondnum 
print(addition(4, 5))

# 2. Create a lambda that calculates the square of a number.
square = lambda num: num ** 2
print(square(6))

# 3. Create a lambda that returns the greater of two numbers.
bigger = lambda num1, num2: num1 if num1 > num2 else  num2
print(bigger(2, 7))

# 4. Create a lambda that adds 10 to a given number.
plus_ten = lambda num: num + 10 
print(plus_ten(8))

# 5. Create a lambda that returns the last character of a string.
last_char = lambda word: word[-1]
print(last_char("domain"))

# 6. Create a lambda that indicates whether a word has more than 6 letters.
longitude = lambda word: True if len(word) > 6 else False
print(longitude("hair"))

# 7. Create a lambda that converts a string to lowercase.
lower_case = lambda word: word.lower()
print(lower_case("HOnDUras"))

# 8. Create a lambda that returns True if a number is positive.
positive = lambda num: True if num >= 0 else False
print(positive(-5))

# 9. Create a lambda that returns "Empty string" if the string is empty.
empty_string = lambda word: "Cadena vacía" if word == "" else word
print(empty_string(""))

# 10. Create a lambda that calculates the final price with a 21% tax added.
added_tax = lambda price: price * 1.21          #price + price * 0.21
print(added_tax(128))
