#
# Clase 2023-03-27
#

#
# Ex 1: Crea un programa en el que metas por teclado un país,
#       habrá dos funciones:
#       1. una que recoja el país y te dé uno predeterminado si no lo hay
#       2. y uno que entregue un mensaje al usuario
#
# Bonus: Busca la manera de que consulte una lista de países,
#       si no está entre ellos intenta que coja el predeterminado
#
import requests     # pip install requests
from lxml import etree  # pip install lxml
                        # ref: https://lxml.de/parsing.html


def mostrar_poblacion(pais="españa"):
    headers_ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    s = requests.Session()
    url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_población"
    r = s.get(url, headers=headers_ua)

    doc = etree.HTML(r.text)
    countries = doc.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/*')     # Buscamos contenido utilizando XPATH.
                                                                                    # Extraemos todos los TR de la tabla
                                                                                    # que es dónde se muestran los paises
                                                                                    # Ref: https://es.wikipedia.org/wiki/XPath

    encontrado = False
    i = 0
    while i < len(countries) and not encontrado:
        c = countries[i]
        nombre = c.xpath('td[2]/a/text()')   # Leemos la segunda columna TD que es donde viene el nombre
        if len(nombre) > 0:
            if nombre[0].lower() == pais.lower():
                poblacion = c.xpath('td[3]/text()')     # Leemos la tercera columna que es donde viene la población y
                                                        # devolvemos el texto con text()
                cuando = c.xpath('td[10]/text()')     # Leemos la tercera columna que es donde viene la población
                if len(poblacion) > 0:
                    v = (nombre[0], poblacion[0].replace(" ", '.'), cuando[0])
                    print("La población de ", v[0], " es de ", v[1], " habitantes (a fecha de ", v[2], ")", sep="")
                    encontrado = True

        i += 1

    if not encontrado:
        print("Pais no encontrado.")

def detalle_pais(pais):
    mostrar_poblacion(pais)


print("Busca la población de un país")
p = ""
while p == "":
    p = input("País: ")

detalle_pais(p)
