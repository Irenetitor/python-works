import re

# 1. Busca si una cadena empieza por "Hola".

text = "Hola Python"
match = re.match("Hola", text)
print(match)

# 2. Busca la palabra "Python" en una cadena aunque esté en minúsculas.

text = "Estoy aprendiendo python"
search = re.search("Python", text, re.I)
print(search is not None)

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.

text = "Este curso es un curso de Python intermedio"
results = re.findall("curso", text)
print(results)

# 4. Reemplaza todas las apariciones de "lección" por "LECCIÓN".

text = "Esta lección es importante. Otra lección vendrá después."
new_text = re.sub("lección", "LECCIÓN", text)
print(new_text)

# 5. Divide un texto en partes separadas por comas.

text = "Uno,Dos,Tres,Cuatro"
parts = re.split(",", text)
print(parts)

# 6. Busca la primera palabra que comience con "A" o "a".

text = "Ayer aprendí algo nuevo"
match = re.search(r"\b[aA]\w+", text)
print(match.group())

# 7. Encuentra todas las palabras en una cadena que terminen en "ción".

text = "Educación, programación y diversión"
results = re.findall(r"\w+ción", text)
print(results)

# 8. Verifica si una cadena contiene solo números.

text = "123456"
match = re.fullmatch(r"\d+", text)
print(match is not None)

# 9. Reemplaza todos los números de una cadena por el texto "[número]".

text = "Estoy aprendiendo 2 lenguajes y 3 frameworks"
new_text = re.sub(r"\d+", "[número]", text)
print(new_text)

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.

text = "Este dato vale oro en esta clase"
results = re.findall(r"\b\w{4}\b", text)
print(results)
