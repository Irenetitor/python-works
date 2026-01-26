import math
import numpy
import pandas
import requests
from mypackage import arithmetics

# 1. Importa el módulo math y muestra el valor de pi.

# import math
print("El valor de pi es:", math.pi)

# 2. Crea un array de números usando numpy y multiplícalo por 3.

# import numpy
array = numpy.array([10, 20, 30])
print(array * 3)

# 3. Muestra la versión instalada de numpy.

# import numpy
print("Versión de numpy:", numpy.version.version)

# 4. Realiza una petición HTTP con requests a una API pública y muestra el código de estado.

# import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
print("Código de estado:", response.status_code)

# 5. Importa una función llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilízala.

# from mypackage import arithmetics
print(arithmetics.sum_two_values(3, 7))  # 10

# 6. Usa pandas para crear un DataFrame con nombres en español.

# import pandas
data = {"Nombre": ["Brais", "Sara"], "Edad": [37, 45]}
df = pandas.DataFrame(data)
print(df)

# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.

# pip install requests

# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros Pokémon.

# import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
data = response.json()
names = [p["name"] for p in data["results"]]
print("Nombres:", names)

# 9. Muestra todos los paquetes instalados con pip desde la terminal.

# pip list

# 10. Escribe una línea de código que muestre la ayuda sobre el paquete numpy desde Python.

# import numpy
help(numpy)
