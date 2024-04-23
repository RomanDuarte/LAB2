"""Escribe una función llamada es_primo que tome un número como argumento y
devuelva True si es primo y False si no lo es."""

def es_primo(numero):
    if numero <= 1: #los numeros primos deben ser mayores a 1
        return False
    elif numero == 2: #el numero 2 es primo
        return True
    elif numero % 2 == 0:#los numeros pares mayores que 2 no son primos
        return False
    else:
        for i in range(3,int(numero**0.5)+1, 2):
            if numero % i == 0:
                return False
        return True
    
numero = 17
print("¿Es", numero, "un número primo?", es_primo(numero))



