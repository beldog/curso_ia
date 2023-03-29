#
# Clase 2023-03-29
#

#
# Ex: Clases y Objetos
#

import datetime as dt


class Alumno:

    def __init__(self, dni, fecha):
        self.dni = dni
        self.fecha = fecha

    def __str__(self):
        return f"{self.dni} - {self.fecha.strftime('%d/%m/%Y')}"


curso = []


def alta_alumno():
    dni = ""
    fecha = None
    while dni == "" or fecha is None:
        try:
            dni = input("DNI: ")
            f = input("Fecha de matriculación (dd-mm-aaaa): ")
            if f == "":
                fecha = dt.datetime.now()
            else:
                fecha = dt.datetime.strptime(f, "%d-%m-%Y")
        except:
            print("\t!!! El valor no es correcto")

    alumno = Alumno(dni, fecha)
    return alumno


def listar_matriculados(curso):
    if len(curso) > 0:
        print("Los alumnos matriculados al curso son:")
        print(curso)    # Imprimimos el array para confirmar que los alumnos son instancias de la clase Alumno

        i = 1
        for a in curso:
            print(f"\t({i}) {a.dni} - {a.fecha.strftime('%d/%m/%Y')}")
            i += 1
    else:
        print("No hay ningún matriculado")


print("\nElige la opción:"
      "\n\t(N) Nuevo alumno"
      "\n\t(L) Listar alumnos"
      "\n\t(S) Salir"
      "\n\tCualquier otra tecla para volver a mostrar este menú.",
      sep="")

estado = True
while estado:
    t = input("\n> ")

    if t.lower() == "n":
        curso.append(alta_alumno())
    elif t.lower() == "l":
        listar_matriculados(curso)
    elif t.lower() == "s":
        estado = False
    else:
        print("\nElige la opción:"
              "\n\t(N) Nuevo alumno"
              "\n\t(L) Listar alumnos"
              "\n\t(S) Salir"
              "\n\tCualquier otra tecla para volver a mostrar este menú.",
              sep="")
else:
    print("Bye")
