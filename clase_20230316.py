# Clase 2023-03-16

#
# Ex 1: Trabajo condicionales
#

# import random as rd
#
# repetir = True
# while repetir:
#     accion = input("Elige 0 para encender, 1 para apagar, 2 para standby: ")
#
#     if accion == "0":
#         repetir = False
#         print("Aire encendido")
#
#         temp = rd.randrange(1, 45) #temp = int(input("Temperatura: "))
#         # print("Cambiando temperatura a " + str(temp) + "º")
#
#         msg = ""
#         if temp < 10: msg = "Hace mucho frío"
#         elif temp < 20: msg = "Hace frío"
#         elif temp < 30: msg = "Hace calor"
#         elif temp < 40: msg = "Hace mucho calor"
#         elif temp < 50: msg = "Ola de calor"
#
#         msg += " " + str(temp) + "º"
#         print(msg)
#
#     elif accion == "1":
#         repetir = False
#         print("Aire apagado")
#     elif accion == "2":
#         repetir = False
#         print("Aire en standby")

# #
# # Ex 2: Listas
# #
#
# list1 = ["apple", "banana", "cherry"]
# list2 = list1.copy()
#
# #mostramos lista/elemento
# print(">> Mostramos lista/elemento")
# print(list1)
# print(list1[0])
#
# #añadimos elementos
# print("\n>> Añadimos elementos")
# list1.append("pear")
# print(list1)
#
# #editamos elementos
# print("\n>> Editamos elementos")
# list1[1] = "pear"
# print(list1)
#
#
# #eleminamos elementos
# print("\n>> Eliminamos elementos")
# list1.remove("cherry")
# print(list1)
#
# list1.pop(0)
# print(list1)
#
# #iteramos
# print("\n>> Mostrando todos los elementos")
# i = 0
# for l in list2:
#     print(i, "-", l)
#     i += 1
#
# #
# # Ex 2: Tuplas
# #
# tupla1 = ("apple", "banana", "cherry")
#
# #mostramos tupla/elemento
# print(">> Mostramos tupla/elemento")
# print(tupla1)
# print(tupla1[0])


#
# Ex 3: Crear dos listas y modifica algún elemento y muestra los elementos de una determinada posición
#

nombres = ["Juan", "Mario", "María", "Jorge", "Ian"]
edades = [10, 20, 35, 40, 3]

print("Nombres: ", nombres)
print("Edades: ", edades)

edades[3] = 41
nombres[3] = "Jorge Javier"

elemento = 3
print("Valores cambiados: ", nombres[elemento], "-", edades[elemento])

# print("\nListamos todos los datos:")
# i = 0
# for n in nombres:
#     print(n, "-", edades[i])
#     i += 1

