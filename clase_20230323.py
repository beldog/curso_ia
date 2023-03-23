#
# Clase 2023-03-23
#

#
# ar=["raúl", "hector", "pedro"]
#
# nombre = input("Indica el nombre a buscar: ")
#
# i=0
#
# while i<len(ar):
#     if ar[i]== nombre:
#         print(nombre, "está en la posición:", str(i+1))
#         break
#     else:
#         print("no es", nombre)
#     i+=1


# #
# # Ex: Continue, Pass, break
# #
# ar=["raúl", "hector", "pedro"]
#
# nombre = input("Indica el nombre a buscar: ")
#
# i=0
#
# while i<len(ar):
#
#     if ar[i]== nombre:
#         break
#     elif ar[i] == "otro":
#         pass
#     else:
#         i+=1
#         continue
#
# else:
#     print("Fin del programa")
#
# print("Test")
    

#
# Ex 1: Crea un cine en el que:
# - recojas el nombre y dni del espectador.
# - muestres una lista de espectadores con su nº de asiento correspondiente.
# - Almacénalo en una lista inmutable, y sal del programa
# opcional: borra espectadores, sustituye espectadores en la misma posición
#
import random as rd

BUTACAS = 5
cine = []
espectador = ()


#
# Función para asignar butacas libres
# Devuelve: valor mayor de 0 si ha encontrado una butaca libre; sino 0
def asignar_butaca():
    b = 0

    if len(cine) <= BUTACAS-1: # comprobamos si aún quedan butacas libres
        while b == 0:
            b = rd.randrange(1, BUTACAS+1)

            # Confirmamos que la butaca no está en uso
            # si lo está buscamos otra butaca
            i = 0
            while i < len(cine):
                if cine[i][2] == b:
                    b = 0
                i += 1

    return b

#
# Función para buscar espectadores a partir de su DNI
# Devuelve: el índice donde se ha encontrado al espectador; -1 si no se encuentra
def buscar_espectador(dni):
    e = -1

    encontrado = False
    i = 0
    while i < len(cine) and not encontrado:
        if cine[i][1] == dni:
            e = i
            encontrado = True
        i += 1

    return e

estado = True
while estado:
    t = input("\nElige la opción:"
              "\n\t(N) Nuevo espectador"
              "\n\t(U) Cambiar butaca"
              "\n\t(B) Borrar espectador"
              "\n\t(C) Consultar el cine"
              "\n\t(S) Salir"
              "\n\t>>> ")

    if t.lower() == "n":
        # Controlamos que hayamos podido asignar una butaca
        butaca = asignar_butaca()
        if butaca > 0:
            nombre = input("Nombre: ")
            dni = input("DNI: ")

            espectador = (nombre, dni, butaca)
            cine.append(espectador)

            print("Te hemos asignado la butaca ", butaca, " ¡Que disfrutes la película!")
        else:
            print("!!!El cine está lleno :(")

    elif t.lower() == "u":
        butaca = asignar_butaca()
        if butaca > 0:
            dni = input("DNI del espectador: ")
            index = buscar_espectador(dni)

            if index > -1:
                temp = list(cine[index])
                temp[2] = butaca
                cine[index] = tuple(temp)
                print("Butaca", temp[2], "asignada.")
            else:
                print("\t!!!El espectador no se ha encontrado.")
        else:
            print("!!!El cine está lleno :(")

    elif t.lower() == "b":
        dni = input("DNI del espectador: ")
        index = buscar_espectador(dni)

        if index > -1:
            e = cine[index]
            cine.pop(index)
            print("Usuario", e, "borrado.")
        else:
            print("\t!!!El espectador no se ha encontrado.")

    elif t.lower() == "c":
        print("Los espectadores son: ")
        for e in cine:
            print("\t", e)

    elif t.lower() == "s":
        estado = False
    else:
        print("\t!!!Esta opción no está disponible. Vuelve a intentarlo")
else:
    print("La película ha terminado. ¡Feliz día!")
