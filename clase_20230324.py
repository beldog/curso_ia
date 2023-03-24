#
# Clase 2023-03-24
#

# #
# # Ex: Funciones
# #
#
# # Función que imprime un texto
# def mi_funcion():
#     print("Hola, soy tu función")
#
# mi_funcion()
#
#
# # Función que recibe un nombre e imprime un texto con dicho nombre
# def mi_funcion(nombre):
#     print("Hola ", nombre, ", soy tu función", sep="")
#
# nombre = "Pepe"
# mi_funcion(nombre)
#
# n1 = 10
# n2 = 20
#
# # Función para sumar dos números
# def sumar(x, y):
#     print(x+y)
#     x +=1
#
# sumar(n1, n2)
# print(n1)

# #
# # Ex 1: Definir 3 funciones: sumar, restar y multiplicar
# #
# import locale
#
# locale.setlocale(locale.LC_ALL, 'es_ES')
#
#
# # Suma valores
# def sumar(x, y):
#     return x + y
#
#
# # Resta valores
# def restar(x, y):
#     return x - y
#
#
# # Multiplicar valores
# def multiplicar(x, y):
#     return x * y
#
#
# # Recoge dos números enteros por teclado
# # Devuelve: int, int
# def recoger_numeros():
#     x = ""
#     y = ""
#
#     while x == "" or y == "":
#         try:
#             x = int(input("Primer número: "))
#             y = int(input("Segundo número: "))
#         except:
#             print("\t!!!Los valores no son números.")
#
#     return x, y
#
#
# estado = True
# while estado:
#     t = input("\nElige la opción:"
#               "\n\t(+) Sumar"
#               "\n\t(-) Restar"
#               "\n\t(*) Multiplicar"
#               "\n\t(S) Salir"
#               "\n\t>>> ")
#
#     if t == "+":
#         n1, n2 = recoger_numeros()
#         result = sumar(n1, n2)
#         print(n1, "+", n2, "=", result)
#
#     elif t == "-":
#         n1, n2 = recoger_numeros()
#         result = restar(n1, n2)
#         print(n1, "-", n2, "=", result)
#
#     elif t == "*":
#         n1, n2 = recoger_numeros()
#         result = multiplicar(n1, n2)
#         txt = "{:,} * {:,} = {:,}"
#         print(txt.format(n1, n2, result))   # Damos formato de número (separando millares) al string que imprimimos
#                                             #   referencia: https://www.w3schools.com/python/ref_string_format.asp
#                                             #
#                                             # Para entornos ingleses el separador de millares es la coma (,)
#                                             #   para entornos españoles el separador de millares es el pinto (.)
#                                             #   Para cambiar el idioma hay que forzar el cambio del LOCALE
#                                             #   referencia: https://docs.python.org/3/library/locale.html?highlight=locale#module-locale
#
#     elif t.lower() == "s":
#         estado = False
#
#     else:
#         print("\t!!!Esta opción no está disponible. Vuelve a intentarlo")
# else:
#     print("¡Feliz día!")


#
# EX 2: Comprueba la temperatura caso por caso, y usa funciones que sumen o resten 10º,
#       según la temperatura que resulte el mensaje cambiará
#

MIN = -50
MAX = 50

temperatura = 0
incremento = 10

# Sube la temperatura t grados
# Devuelve: el valor de la temperatura tras sumar t
def subir(t = 1):
    r = temperatura + t
    if r > MAX:
        raise Exception("Has llegado al límite")

    return r

# Baja la temperatura t grados
# Devuelve: la nueva temperatura tras restart t
def bajar(t = 1):
    r = temperatura - t
    if r < MIN:
        raise Exception("Has llegado al límite")

    return r


# Muestra la barra de temperatura
def mostrar_temperatura():
    print("[", sep="", end="")

    i = MIN
    while i <= MAX:
        if i == 0:
            print("0", sep="", end="")
        else:
            if i <= temperatura:
                print("#", sep="", end="")
            else:
                print("-", sep="", end="")
        i += 1
    else:
        print("] ", temperatura, " ªC", sep="")


print("\nElige la opción:"
      "\n\t(+) Subir 10ºC"
      "\n\t(-) Bajar 10ºC"
      "\n\tCualquier otra tecla para ver la Temperatura actual"
      "\n\t(S) Salir")

estado = True
while estado:
    t = input(": ")

    if t == "+":
        try:
            temperatura = subir(incremento)
            mostrar_temperatura()
        except:
            print("\t!!! No se puede subir más la temperatura")
    elif t == "-":
        try:
            temperatura = bajar(incremento)
            mostrar_temperatura()
        except:
            print("\t!!! No se puede bajar más la temperatura")

    elif t.lower() == "s":
        estado = False

    else:
        mostrar_temperatura()
else:
    print("Bye")