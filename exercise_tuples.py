# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).
    """
    return registro[1]


def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").
    """
    return (coordenada[0], coordenada[1])


def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.
    """
    coord_azara = registro_azara[1]
    coord_rui = registro_rui[1][0] + registro_rui[1][1]
    if coord_azara == coord_rui:
        return registro_azara + registro_rui
    return "not a match"


def sum_tuple(numeros):
    """
    Recorre la tupla de números y retorna la suma total.
    """
    total = 0
    for n in numeros:
        total += n
    return total


def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.
    """
    contador = 0
    for item in tupla:
        if item == elemento:
            contador += 1
    return contador


def find_index(tupla, elemento):
    """
    Recorre la tupla y retorna el índice de la PRIMERA aparición del elemento.
    """
    for i in range(len(tupla)):
        if tupla[i] == elemento:
            return i
    return -1


def filter_positives(numeros):
    """
    Recorre una tupla de números y retorna una nueva tupla con solo los números positivos.
    """
    positivos = []
    for n in numeros:
        if n > 0:
            positivos.append(n)
    return tuple(positivos)