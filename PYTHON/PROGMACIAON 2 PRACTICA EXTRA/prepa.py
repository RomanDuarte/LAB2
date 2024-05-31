"""cursos"""
from parcial_disponibles import *
empleados= []
cursos = cursos_disponibles

"""caso1"""

def caso1():
    nombre =str(input("ingrese su nombre: "))
    while True:
        legajo =str(input("ingrese su legajo: "))
        if len(legajo) != 5:
            print("el legajo debe tener 5 caracteres")
        else:
            break
    antiguedad =int(input("ingrese su antiguedad: "))
    if antiguedad < 6:
        print("la antiguedad debe ser mayor a 6")
    else:
        empleados.append({"nombre":nombre,"legajo":legajo,"antiguedad":antiguedad,"cursos":[]})
    print("\ncompletado")

"""caso2"""

def caso2():
    buscar_legajo = input("ingrese su legajo: ")
    encontrados = False
    for diccionario in empleados:
        if diccionario["legajo"] == buscar_legajo:
            encontrados=True
            while True:
                print("1:agregar curso: ")
                print("2.finalizar")
                opcion=input("selecionar una opcion")
                if opcion == "1":
                    for i,cursos in enumerate(cursos_disponibles,1):
                        print(f"{i},{cursos}")
                    valores = input("seleccione un curso o ponga 0 para salir: ")
                    if valores == 0:
                        print("no se agrego ningun curso")
                        break
                    elif int(valores) in range(1,len(cursos_disponibles)+1):
                        cursos_selecionados = cursos_disponibles[int(valores)-1]
                        diccionario["cursos"].append(cursos_selecionados)
                        print("curso agregado correctamente")
                elif opcion == "2":
                    break
                else:
                    print("opcion invalida")
            break
    if not encontrados:
        print("no se encontro ningun empleado")
    print("finalizado")


"""caso3"""

def caso3():
    if empleados:
        empleados_ordenados = sorted(empleados, key=lambda x: len(x["cursos"]), reverse=True)
        print(f"\nResumen de empleados")
        for empleado in empleados_ordenados:
            print("Nombre:", empleado["nombre"])
            print("Legajo:", empleado["legajo"])
            print("Cantidad de cursos realizados:", len(empleado["cursos"]))
            print("Cursos realizados:", empleado["cursos"])
            print("Antiguedad:",empleado["antiguedad"])
    else:
        print("No hay empleados registrados.")


"""menu"""
while True:
    print("\nelija la opcion a elejir")
    print("1. registrar empleados")
    print("2. agregar nuevo curso")
    print("3. mostrar resultado")
    print("4. salir")
    opcion = input()
    if opcion == "1":
        caso1()
    elif opcion == "2":
        caso2()
    elif opcion == "3":
        caso3()
    elif opcion == "4":
        break
    else:
        print("opcion incorrecta, vuelva a intentarlo")