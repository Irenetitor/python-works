# 1. Import the math module and display the value of pi.
import math
print(math.pi)

# 2. Create an array of numbers using numpy and multiply it by 3.
import numpy as np
array = np.array([3, 4, 5, 6])
print(array * 3)

# 3. Display the installed version of numpy.
print("Numpy's version: ", np.version.version)

# 4. Make an HTTP request with requests to a public API and display the status code.
import requests
response = requests.get("https://dog.ceo/api/breeds/image/random")
print(response.status_code)

# 5. Import a function called sum_two_values from a custom package mypackage.arithmetics and use it.
from arithmetics import sum_two_values
print(sum_two_values(3, 7))


# 6. Use pandas to create a DataFrame with names in Spanish.
import pandas
data = {"Name": ["Irene", "Adriana"], "Age": [34, 33]}
df = pandas.DataFrame(data)
print(df)

# 7. Run the command to install the requests package from the terminal.
#pip install requests

# 8. Use requests to obtain data from an API and extract only the names of the first Dogs.
response = requests.get("https://dog.ceo/api/breeds/list/all")
data = response.json()
names = list(data["message"].keys())[:10]
print("Nombres:", names)


# 9. Display all installed packages with pip from the terminal.
#pip list

# 10. Write a line of code that displays the help for the numpy package from Python.
import numpy
help(numpy)
