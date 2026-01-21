# 1. Create a text file and write the sentence "Hello from Python" in it.

file = open("greeting.txt", "w")
file.write("Hello from Python")
file.close()

# 2. Open a file and read all of its contents.

file = open("greeting.txt", "r")
print(file.read())
file.close()

# 3. Add a new line at the end of the file with the text "Added line".

file = open("greeting.txt", "a")
file.write("\nAdded line")
file.close

# 4. Read only the first 10 characters of the file.

file = open("greeting.txt", "r")
print(file.read(10))
file.close()

# 5. Use seek to return to the beginning of the file and read from there.

file = open("greeting.txt", "r")
file.seek(0)
print(file.read())
file.close

# 6. Read and print the file contents line by line using readline.

file = open("greeting.txt", "r")
print(file.readline())
print(file.readline())
file.close()

# 7. Read all the lines of the file into a list and iterate over them with a loop.

file = open("greeting.txt", "r")
files2 = file.readline()
for file2 in files2:
    print(file2.strip())
file.close()


# 8. Create a new file that overwrites the existing one if it already exists, and write several lines.

file = open("new_file.txt", "w")
file.write("This is a new file/nwhere I'm writing this new content/nCould you give me please an idea")
file.close()

# 9. Use a function to open a file, write text, and close it automatically using with.

with open("with_file.txt", "w") as file:
    file.write("This file is managed by with")

file.close()


# 10. Read a file line by line and display only the lines that contain the word "Python".

with open("greeting.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line)