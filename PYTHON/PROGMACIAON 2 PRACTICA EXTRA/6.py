"""Escribe un programa que itere sobre un diccionario e imprima solo las claves que sean
strings"""

mi_diccionario = {1:"uno","dos": 2,"tres":"three",4:"cuatro"}

print("claves strings: ")
for clave in mi_diccionario:
    if isinstance(clave, str):
        print(clave)