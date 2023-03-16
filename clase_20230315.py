# Clase 2023-03-15

# #
# # Ex 1: if-else
# #
# var1 = 1
#
# print(True == var1)
#
# var2 = input("Edad: ")
# var2 = int(var2)
#
# if var2 == 18:
#     print("Tiene 18 años")
# else:
#     print("No tiene 18 años")


# #
# # Ex 2: if-elif-else
# #
# var = input("Elija la gasolina premium (95, 99, premium): ")
#
# if var == "95":
#     print("Ud. ha elegido gasolina " + var)
# elif var == "99":
#     print("Ud. ha elegido gasolina " + var)
# elif var == "premium":
#     print("Ud. ha elegido gasolina " + var)
# else:
#     print("No ha elegido ninguna opción de las disponibles")


# #
# # Ex 3: boolean
# #
# viento = True
# lluvia = False
# temperatura = 20
#
# if viento and lluvia and temperatura <= 20:
#     print("Hace mal tiempo :(")
# else:
#     print("Hace buen tiempo :)")


#
# Ex 4: boolean como control de estados
#
estado = False
num1 = ""
num2 = ""

print("Suma de dos números")
while not estado:
    num1 = input("Introduce el primer número: ")
    num2 = input("Introduce el segundo número: ")

    if num1 != "" and num2 != "":
        try:
            num1 = int(num1)
            num2 = int(num2)
        except:
            estado = False
            print("No hay números")
        else:
            estado = True
    else:
        estado = False
        print("No hay números")

if estado:
    suma = num1 + num2
    print("Suma: " + str(suma))
