"""Escribe una función llamada contador_letras que tome una cadena como argumento y
devuelva un diccionario donde las claves sean las letras de la cadena y los valores sean
la cantidad de veces que aparece cada letra."""

def contador_letras(cadena):
    # Inicializar un diccionario vacío para almacenar el recuento de letras
    contador = {}
    
    # Iterar sobre cada letra en la cadena
    for letra in cadena:
        # Si la letra ya está en el diccionario, incrementar su contador
        if letra in contador:
            contador[letra] += 1
        # Si la letra no está en el diccionario, agregarla con un contador de 1
        else:
            contador[letra] = 1
    
    return contador

# Ejemplo de uso
cadena_ejemplo = "Hola mundo"
resultado = contador_letras(cadena_ejemplo)
print(resultado)
