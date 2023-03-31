#
# Clase 2023-03-31
#

#
# Ex: Crear en un parking. Un sistema que recoja las matrículas de los coches que entran y salen.
#     Deberás crear la clase de coche, sus atributos, elimina uno de los atributos, diferencia entre
#     métodos que cambien atributos y funciones que sirvan para el resto del programa
#

class Coche:
    def __init__(self, m, modelo):
        self.matricula = m
        self.modelo = modelo
        self.itv = True

    def setitv(self, b):
        self.itv = b

    def __str__(self):
        return f"{self.modelo}-{self.matricula}, ITV: {self.itv}"


parking = []

print("\nElige la opción:"
      "\n\t(A) Aparcar"
      "\n\t(S) Salir"
      "\n\t(P) Mostrar coches aparcados"
      "\n\t(Q) Salir"
      "\n\tCualquier otra tecla para volver a mostrar este menú.",
      sep="")

def nuevo_coche():
    m = input("Matricula: ")
    mod = input("Modelo: ")

    return Coche(m, mod)


def baja_coche(parking, matricula):
    borrado = False
    for c in parking:
        if c.matricula == m:
            parking.remove(c)
            borrado = True
            break

    return borrado


estado = True
while estado:
    t = input("> ")

    if t.lower() == "a":
        parking.append(nuevo_coche())

    elif t.lower() == "s":
        m = input("Matricula: ")
        borrado = baja_coche(parking, m)
        if borrado:
            print("Salida registrada")
        else:
            print("Matricula no encontrada")

    elif t.lower() == "p":
        for c in parking:
            print(c)

    elif t.lower() == "q":
        estado = False

    else:
        print("\nElige la opción:"
              "\n\t(A) Aparcar"
              "\n\t(S) Salir"
              "\n\t(P) Mostrar coches aparcados"
              "\n\t(Q) Salir"
              "\n\tCualquier otra tecla para volver a mostrar este menú.",
              sep="")

else:
    print("Bye")
