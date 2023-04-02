# Entregable:
#  (1) un for que recorra un rango.
#  (2) cuando llegue a cierto número mostrar un mensaje en pantalla
#  (3) Crea un objeto, con al menos 2 propiedades/atributos y cámbiale el valor a uno de ellos.
import random as rd


class ListaAleatoria:
    def __init__(self, size):
        self._posicion = 0
        self._valores = rd.sample(range(1,100), size)   # generamos un array de 10 posiciones

    @property
    def posicion(self):         # Definimos getters and setters utilizando decoradores de propiedad
        return self._posicion   # Ref 1: https://docs.python.org/3/library/functions.html?highlight=property#property

    @posicion.setter
    def posicion(self, value):  # Ref 2: https://www.geeksforgeeks.org/getter-and-setter-in-python/
        self._posicion = value

    @property
    def valores(self):
        return self._valores


r = ListaAleatoria(10)                                                  # (3) Creamos una instancia de la clase
r.posicion = int(input(f"¿Qué posición quieres mostrar? (0-{10-1}): ")) # (3) Actualizamos un atributo de la instancia
i = 0
for v in r.valores:                                                     # (1) For que recorre una lista
    if i == r.posicion:                                                 # (2) Si la iteración = posición elegida
        print(f"El valor de la posición {r.posicion} es: {v}")          # (2) imprimimos el valor de la lista
    i += 1
