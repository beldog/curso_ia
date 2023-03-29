#
# Clase 2023-03-28
#

# #
# # Ex: Tensorflow; https://www.tensorflow.org/tutorials/quickstart/beginner?hl=es-419
# #
#
# import tensorflow as tf
#
# mnist = tf.keras.datasets.mnist
#
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0
#
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28, 28)),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dropout(0.2),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(x_train, y_train, epochs=5)
#
# model.evaluate(x_test,  y_test, verbose=2)

#
# Ex 1: Recoge el dni del usuario y la fecha de matriculación del alumno, almacena la información en una lista
#
import datetime as dt


curso = []


def alta_alumno():
    dni = ""
    fecha = None
    while dni == "" or fecha is None:
        try:
            dni = input("DNI: ")

            ahora = dt.datetime.now()   # Creamos variable con la fecha-hora actual
            print("Fecha de matriculación: ")
            d = int(input("\tDía (1-31): "))
            m = int(input("\tMes: (1-12): "))
            a = int(input(f"\tAño: (1900-{ahora.year}): "))

            fecha = dt.datetime(a, m, d)
        except:
            print("\t!!! El valor no es correcto")

    alumno = {"dni": dni, "fecha": fecha}

    return alumno


def listar_matriculados(curso):
    if len(curso) > 0:
        print("Los alumnos matriculados al curso son:")
        i = 1
        for a in curso:
            print(f"\t({i}) {a.get('dni')} - {a.get('fecha').strftime('%d/%m/%Y')}")
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
