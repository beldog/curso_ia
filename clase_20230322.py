# Clase 2023-03-22

#
# Ex: Selectores para hacer un menú de opciones
#
import random as rd

premio = 0
premios = []

estado = True
while estado:
    t = input("Elige la opción:"
              "\n\t(J) Jugar"
              "\n\t(G) Guardar el último premio"
              "\n\t(A) Jugar y Guardar el premio"
              "\n\t(C) Consultar los premios"
              "\n\t(S) Salir"
              "\n\t>>> ")

    if t.lower() == "j":
        premio = rd.randrange(1, 11)
        print("Te han tocado ", premio, "helado/s :).")
    elif t.lower() == "g":
        premios.append(premio)
    elif t.lower() == "c":
        print("Los premios son: ", premios)
    elif t.lower() == "a":
        premio = rd.randrange(1, 11)
        print("Te han tocado ", premio, "helado/s :).")
        premios.append(premio)
    elif t.lower() == "s":
        estado = False
    else:
        print("\t!!!Esta opción no está disponible. Vuelve a intentarlo")
else:
    print("Fin del Juego. Adiós!")


# #
# # Extra: Selectores para hacer un menú de opciones definiendo funciones para no repetir lógica
# #
# import random as rd
#
# premio = 0
# premios = []
#
#
# def jugar():
#     p = rd.randrange(1, 11)
#     return p
#
#
# def guardar(val):
#     premios.append(val)
#
#
# estado = True
# while estado:
#     t = input("Elige la opción:"
#               "\n\t(J) para Jugar"
#               "\n\t(G) para Guardar el último premio"
#               "\n\t(A) para Jugar y Guardar el premio"
#               "\n\t(C) para Consultar los premios"
#               "\n\t(S) para Salir"
#               "\n\t>>> ")
#
#     if t.lower() == "j":
#         premio = jugar()
#         print("Te han tocado ", premio, "helado/s :).")
#     elif t.lower() == "g":
#         guardar(premio)
#     elif t.lower() == "c":
#         print("Los premios son: ", premios)
#     elif t.lower() == "a":
#         premio = jugar()
#         guardar(premio)
#         print("Te han tocado ", premio, "helado/s :).")
#     elif t.lower() == "s":
#         estado = False
#     else:
#         print("\t!!!Esta opción no está disponible. Vuelve a intentarlo")
# else:
#     print("Fin del Juego. Adiós!")
