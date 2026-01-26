import re

my_sentence = "Hello, each lesson helps you learn Python and includes 10 tests. Lesson six reviews the code, and you have to read it."

# 1. Check if a string starts with "Hello".

match = re.match("Hello", my_sentence, re.I)
print(match)

# 2. Search for the word "Python" in a string even if it is in lowercase.

search = re.search("python", my_sentence, re.I)
print(search)

# 3. Find all occurrences of the word "you" in a string.

findall = re.findall("you", my_sentence, re.I)
print(findall)

# 4. Replace all occurrences of "lesson" with "LESSON".

print(re.sub("[lL]esson", "LESSON", my_sentence))

# 5. Split a text into parts separated by commas.

print(re.split(",", my_sentence))

# 6. Find the first word that starts with "A" or "a".

search2 = re.search(r"\b[aA]\w+", my_sentence)
print(search2)

# 7. Find all the words in a string that end with "son".

findall2 = re.findall(r"\w+son", my_sentence)
print(findall2)

# 8. Check if a string contains only numbers.

text = "87643456"

match2 = re.fullmatch(r"\d+", text)
print(match2)

# 9. Replace all the numbers in a string with the text "[number]".

print(re.sub("\d+", "number", my_sentence))

# 10. Find all words that are exactly 4 letters long in a string.

findall3 = re.findall(r"\b[a-zA-Z]{4}\b", my_sentence)
print(findall3)