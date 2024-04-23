"""Escribe una función llamada eliminar_duplicados que tome una lista como argumento y
devuelva una nueva lista con los elementos únicos de la lista original, manteniendo el
orden"""

def eliminar_duplicado(lista):
    conjunto_sin_duplicar = []
    for elementos in lista:
        if elementos not in conjunto_sin_duplicar:
            conjunto_sin_duplicar.append(elementos)

    return conjunto_sin_duplicar

lista_original=[1, 2, 3, 4, 2, 3, 5, 6, 1,6,6,6]
resultado = eliminar_duplicado(lista_original)
print(resultado)