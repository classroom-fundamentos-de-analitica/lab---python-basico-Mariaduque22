"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/214
    """
    suma=0
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            suma+= int(row[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registros = []
    columna = []
    letra=[]

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
                columna.append(row[0])
                if(not row[0] in letra):
                    letra.append(row[0])
    letra.sort()
    for i in letra:
        registros.append((i, columna.count(i)))

    return registros


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    contador = []
    letra=[]
    suma=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not row[0] in letra):
                contador.append(int(row[1]))
                letra.append(row[0])
            else:
                contador[letra.index(row[0])]+=int(row[1])
    for i in letra:
        suma.append((i,contador[letra.index(i)]))
    suma.sort(reverse=False)
    return suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros = []
    mes=[]
    columna = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            numero_mes = row[2].split("-")[1]
            columna.append(numero_mes)
            if(not numero_mes in mes):
                mes.append(numero_mes)
    mes.sort()
    for i in mes:
        registros.append((i, columna.count(i)))
    return registros


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    val_maximo = []
    val_minimo = []
    letras=[]
    maximos = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not row[0] in letras):
                letras.append(row[0])
                val_maximo.append(int(row[1]))
                val_minimo.append(int(row[1]))
            else:
                if(val_maximo[letras.index(row[0])]<int(row[1])):
                    val_maximo[letras.index(row[0])]=int(row[1])
                if(val_minimo[letras.index(row[0])]>int(row[1])):
                    val_minimo[letras.index(row[0])]=int(row[1])
    for letra in letras:
        maximos.append((letra,val_maximo[letras.index(letra)],val_minimo[letras.index(letra)]))
    maximos.sort(reverse=False)
    return maximos

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    diccionario = []
    letras=[]
    val_maximo = []
    val_minimo = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for clave in row[4].split(','):
                letra = clave.split(':')[0]
                codigo = clave.split(':')[1]
                if(not letra in letras):
                    letras.append(letra)
                    val_maximo.append(int(codigo))
                    val_minimo.append(int(codigo))
                else:
                    if(val_maximo[letras.index(letra)]<int(codigo)):
                        val_maximo[letras.index(letra)]=int(codigo)
                    if(val_minimo[letras.index(letra)]>int(codigo)):
                        val_minimo[letras.index(letra)]=int(codigo)
    for i in letras:
        diccionario.append((i,val_minimo[letras.index(i)],val_maximo[letras.index(i)]))
    diccionario.sort(reverse=False)
    return diccionario


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    orden = []
    letras = []
    asociacion = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not int(row[1]) in orden):
                letras.append([row[0]])
                orden.append(int(row[1]))
            else:
                letras[orden.index(int(row[1]))].append(row[0])
    for i in orden:
        asociacion.append((i,letras[orden.index(i)]))
    asociacion.sort(reverse=False)
    return asociacion


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    tupla = []
    numero = []
    letra = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not int(row[1]) in numero):
                numero.append(int(row[1]))
                letra.append([row[0]])
            else:
                if(not row[0] in letra[numero.index(int(row[1]))]):
                    letra[numero.index(int(row[1]))].append(row[0])

    for i in numero:
        segunda = letra[numero.index(i)]
        segunda.sort()
        tupla.append((i,segunda))
    tupla.sort(reverse=False)
    return tupla


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dictionario = {}
    columna = []
    registros = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for cod in row[4].split(','):
                letra = cod.split(':')[0]
                columna.append(letra)
                if( not letra in registros):
                    registros.append(letra)
    registros.sort()
    for i in registros:
        dictionario.update({i: columna.count(i)})
    return dictionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    letras=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            columna_4 = row[3].split(",")
            columna_4 = len(columna_4)
            columna_5 = row[4].split(",")
            columna_5 = len(columna_5)
            letras.append((row[0], columna_4, columna_5))
    return letras

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma={}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for letra in row[3].split(","):
                if(not letra in suma.keys()):
                    suma.update({letra: int(row[1])})
                else:
                    suma[letra] += int(row[1])
    diccionario = dict(sorted(suma.items()))
    return diccionario


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma={}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            letra=row[0]
            for clave in row[4].split(","):
                valor = int(clave.split(":")[1])
                if(not letra in suma.keys()):
                    suma.update({letra: valor})
                else:
                    suma[letra] += valor
    diccionario = dict(sorted(suma.items()))
    return diccionario

