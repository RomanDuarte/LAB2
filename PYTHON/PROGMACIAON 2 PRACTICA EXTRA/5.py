"""Escribe un programa que tome dos tuplas e imprima un diccionario donde las primeras
tuplas sean las claves y las segundas tuplas sean los valores correspondientes."""

def tuplas_a_diccionario(tupla_claves, tupla_valores):
    # Verificar si las tuplas tienen la misma longitud
    if len(tupla_claves) != len(tupla_valores):
        return "Las tuplas no tienen la misma longitud"
    
    # Crear el diccionario
    diccionario = {}
    for i in range(len(tupla_claves)):
        diccionario[tupla_claves[i]] = tupla_valores[i]
    
    return diccionario

# Ejemplo de uso
tupla_claves = ('uno', 'dos', 'tres') 
tupla_valores = (1, 2, 3)

resultado = tuplas_a_diccionario(tupla_claves, tupla_valores)
print(resultado)
