# Clase 2023-03-21

# #
# # Ex: Iteraciones y Bucles
# #
# i = 1
#
# while i<5:
#     print(i)
#     i += 1

# #
# # Ex: Crea un bucle while que recorra números desde y haste dos valores introducidos por el usuario
# #
# print("\nListar números entre dos valores")
# print("--------------------------------")
#
# n_min = ""
# n_max = ""
#
# while n_min == "" or n_max == "":
#     try:
#         n_min = int(input("Introduce el número inicial: "))
#         n_max = int(input("Introduce el número final: "))
#     except:
#         print("El valor introducido no es numérico. Vuelve a introducirlo.")
#
# i = n_min
# message = ""
# while i <= n_max:
#     message += str(i)
#     if i != n_max:
#         message += ", "
#     i += 1
#
# print("Número consecutivos desde ", n_min, "-", n_max, ": ", message)


# #
# # Ex: For loop
# #
# import random as rd
#
# print("Listamos los elementos con un for: ")
# colores = "azul negro rojo amarillo rosa".rsplit(" ")
# # print(colores)
# for c in colores:
#     print(c)
# else:
#     print("Fin del \"for\"")
#
# print("\nListamos los elementos con un while: ")
# i = 0
# while i < len(colores):
#     print(colores[i])
#     i += 1
# else:
#     print("Fin del \"while\"")
#
# var = ""
# for x in "bananas":
#     var += x
#     print(x)
#
#     # añadimos esta condición para demostrar que cuando se ejecuta el "break" el "else" del bucle no se ejecuta
#     if rd.randrange(1,100) > 50:
#         break
# else:
#     print(var)

#
# Ex 2: Recorre dos lista con un "for" y muestra diferentes combinaciones
#
print("\nEx 2: Mostramos todas las combinaciones existentes de dos listas")
print("----------------------------------------------------------------")
l1 = "rojo,amarillo,azul,negro,blanco".rsplit(",")
l2 = "casa,puente,armario".rsplit(",")

len1 = len(l1)
len2 = len(l2)

print("Lista 1: ", l1, len1, "elementos.")
print("Lista 2: ", l2, len2, "elementos.")

total = len1*len2
print("\nHay", total, "combinaciones")

i = 1
for x in l1:
    for y in l2:
        print(i, ": ", x, "-", y, sep="")   # ajustamos el separador de variables (sep="")
                                            # para que el texto se imprima bien en consola
                                            # referencia en https://docs.python.org/3.11/library/functions.html#print
        i += 1


#
# Ex 3 (Bonus track): Crea dos dados, informando de las caras por teclado, tira los dados y suma los resultados
#
import random as rd

print("\nEx 3 (Bonus track): Tiramos dos dados y sumamos su resultado")
print("----------------------------------------------")

# Almacenamos los dados en una lista y para cada elemento de la lista
# guardamos sus propiedades: caras y tirada.
# [
#   {"nombre": "SSS", "caras": x, "tirada": y},
#   {"nombre": "SSS", "caras": x, "tirada": y},
#   ...
#   {"nombre": "SSS", "caras": x, "tirada": y}
# ]

dados = []

total = int(input("¿Cuántos dados quieres?: "))

i = 1
while i <= total:
    print("\nIntroduce los datos para el dado ", i, ":", sep="")

    caras = 0
    repetir = True
    while repetir:
        try:
            caras = int(input("Caras del dado (mayor o igual a 4): "))

            if caras <= 3:
                raise Exception("Number too low")

            nombre = "D-"+str(i)
            tirada = rd.randrange(1, caras) # Tiramos el dado para que nos de un valor
            dados.append({"nombre": nombre,
                          "caras": caras,
                          "tirada": tirada})

            repetir = False # Terminamos el bucle para el dado actual
        except:
            print("\t!!! El valor tiene que ser un número entero y mayor de o igual a 4.")

    i += 1

print("\nLos dados son:", dados)

suma = 0
for d in dados:
    t = d.get("tirada")

    print("La tirada del dado", d.get("nombre"), "ha sido: ", t)
    suma += t

print("\nLa suma de las tiradas es: ", suma)
