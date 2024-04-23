"""Escribe un programa que tome una lista de números y devuelva solo los números pares."""

pares = list(range(1,11))
num=[]
for i in pares:
    if  i % 2 == 0:
        num.append(i)
print(num)
