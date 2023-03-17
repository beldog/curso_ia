# Clase 2023-03-17

#
#  Ex: Manipulación de listas
#

l1 = [1, 2, 3]
l2 = ["Ronaldo", "Juan", "Alfonso"]
l3 = [True, False, True]

print(l1, l2, l3)

nombres = []

var1 = input("¿Cuál es tu nombre?: ")
l2.append(var1)
nombres.append(var1)
print(nombres, l2)

print("Tienes", len(nombres), "nombre/s en la lista.") # Mostramos la dimensión de la lista (cuántos elementos tiene)

print("El tipo de tu variable es: ", type(nombres)) # Mostramos el tipo de varible

print("El último elemento es: ", l2[-1]) # Mostramos el último elemento
print("Elementos de la posición 1-3 son: ", l2[1:3]) # Mostramos sólo los valores en los índices del 1 al 2
print("Elementos del 0-2 son: ", l2[:3]) # Mostramos sólo los elementos desde el inicio hasta el índice 2

# Comprobamos si un valor existe en la lista
if "Juan" in l2:
    print("Juan está en la lista")
else:
    print("Juan no está en la lista")

# Actualizamos varios elementos en la lista
l2[1:3] = ["María", "Mario"]
print("La lista actualizada es", l2)

# Añadimos elementos en una índice, los elementos posteriores se desplazan
l2.insert(0, "Jorge")
print("Lista con nombre insertado al principio: ", l2)

# Añadimos al final de la lista l2 la variables nombres (que es una lista)
# y mostramos el valor del primer índice del último elemento de la lista l2
l2.append(nombres)
print("Este es el primer valor del último elemento de la lista: ", l2[-1][0])

# Creamos una lista con los carácteres de una palabra
aux = []
aux.extend("MANGOA")
print("Lista creada a partir de un texto: ", aux)

t1 = (1, 2, 3) # creamos una tupla
aux.extend(t1) #extendemos la lista aux con los valores de la tupla
print("Unimos dos listas: ", aux)

# Eliminamos el primer elemento que encuentre
try:
    aux.remove("A")
    print("Eliminamos el elemento 'O': ", aux)
except:
    print("El elemento no existe")

# Eliminamos el elemento del índice indicado
try:
    aux.pop(1)
    print("Eliminamos el elemento del índice 1: ", aux)
except:
    print("El índice no existe")

# Eliminamos y vaciamos listas
aux2 = aux
print("Valores de la lista aux2: ", aux2)
try:
    del aux2 # eliminamos la variable aux por completo
    print("Valores de la lista aux2 tras eliminarla: ", aux2)
except:
    print("La variable aux2 no está definida")

aux.clear()
print("valores de la lista tras vaciarla: ", aux)


#
# Ex 2: Juntar dos listas y borrar un elemento por su nombre
#
print("\n\nEjercicio 2")
print("-----------")
l1 = "Manolo Violeta María Juan Pedro".rsplit(" ")
l2 = "Rosa Margarita Tulipán".rsplit(" ")
print("Listas a utilizar: ", l1, l2)

l3 = []
l3.extend(l1)
l3.extend(l2)
print("Lista extendida: ", l3)
i = l3.index("Violeta") # Buscamos el índice donde se encuentra el elemento "Violeta"
print("El elemento \"Violeta\" se encuentra en el índice: ", i)
l3.pop(i) # Borramos el elemento
print("Lista tras borrar el elemento Violeta: ", l3)

#
# Ex 2b: Crea dos listas en las que añadas 1 elemento decidido por teclado,
# en caso de que no se envíe nada controla la excepción y obliga al usuario
# a meter datos, junta ambas listas,
#
print("\n\nEjercicio 2b")
print("------------")
estado = True
l1 = (1, 2, 3)
l2 = (2, 4, 6)
print("Las listas a utilizar son: ", l1, l2)

l3 = []
l3.extend(l1)
l3.extend(l2)

while estado:
    elem = input("Introduce un número entero: ")
    if elem != "":
        try:
            numero = int(elem)
            estado = False
        except:
            print("El valor tiene que ser un número entero. Vuélvelo a intentar.")
    else:
        print("No has introducido ningún valor. Vuélvelo a intentar.")

l3.append(numero)
print("La lista final es: ", l3)
