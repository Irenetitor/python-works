### Python Package Manager ###

# PIP https://pypi.org
# pip install pip
# pip --version

from mypackage import arithmetics
import requests
import numpy  # pip install numpy
import pandas  # pip install pandas

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

print(arithmetics.sum_two_values(1, 4))
