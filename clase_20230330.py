#
# Clase 2023-03-30
#

#
# Ex 1: Crea una clase operación_matematica, que pueda sumar, restar, multiplicar y dividir,
#       también necesitamos que se exponga un listado de los resultados
#

import locale   # Librería para gestionar la localización (aka Idioma) del entorno

locale.setlocale(locale.LC_ALL, 'es_ES')    # Definimos el idioma como español (es) de España (ES)


class OperacionesMatematicas:

    def __init__(self, s1, s2):     # Método constructor de la instancia
                                    # Por convenio definimos atributos privados utilizando el prefijo "_" (underscore)
                                    # Ref https://peps.python.org/pep-0008/#method-names-and-instance-variables
        self._n1 = s1
        self._n2 = s2

    # Definimos los métodos/funcionalidades de la clase
    def sumar(self):
        return self._n1 + self._n2

    def restar(self):
        return self._n1 - self._n2

    def multiplicar(self):
        return self._n1 * self._n2

    def dividir(self):
        return self._n1 / self._n2

    def operar(self):
        out = "Los valores a operar son: " + str(self)
        out += "\nSuma: " + str(self.sumar())
        out += "\nResta: " + str(self.restar())
        out += "\nMultiplicación: " + str(self.multiplicar())
        out += "\nDivisión: " + str(self.dividir())

        return out

    def __str__(self):  # Redefinimos el método que representa la instancia
                        # como un texto entendible (string)
        return f"{self._n1} y {self._n2}"


om = None   # variable que será la instancia de la clase OperacionesMatematicas

try:
    n1 = locale.atof(input("Introduce un número: "))    # Utilizamos el método locale.atof() para convertir un string a float
    n2 = locale.atof(input("Introduce otro número: "))  # siguiendo la localización definida por LOCALE (por defecto la del OS)
                                                        # en nuestro caso, hemos definido la localización como es_ES (español de España)
                                                        # para poder interpretar la coma "," como separador de decimales
                                                        # Ref: https://docs.python.org/3/library/locale.html#locale.atof

    om = OperacionesMatematicas(n1, n2)

    print("\nElige la opción:"
          "\n\t(+) Sumar"
          "\n\t(-) Restar"
          "\n\t(*) Multiplicar"
          "\n\t(/) Dividir"
          "\n\t(T) Mostrar todas las operaciones"
          "\n\t(S) Salir"
          "\n\tCualquier otra tecla para volver a mostrar este menú.",
          sep="")

    estado = True
    while estado:
        t = input("> ")

        if t == "+":
            print("Suma:", om.sumar(), ", de", om)
        elif t == "-":
            print("Resta:", om.restar(), ", de", om)
        elif t == "*":
            print("Multiplicación:", om.multiplicar(), ", de", om)
        elif t == "/":
            print("División:", om.dividir(), ", de", om)
        elif t.lower() == "t":
            print(om.operar())
        elif t.lower() == "s":
            estado = False
        else:
            print("\nElige la opción:"
                  "\n\t(+) Sumar"
                  "\n\t(-) Restar"
                  "\n\t(*) Multiplicar"
                  "\n\t(/) Dividir"
                  "\n\t(T) Mostrar todas las operaciones"
                  "\n\t(S) Salir"
                  "\n\tCualquier otra tecla para volver a mostrar este menú.",
                  sep="")
    else:
        print("Bye")

except:
    print("\t!!! Error al recoger los valores.")
