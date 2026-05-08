# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    """
    inventario = {}
    for item in items:
        inventario[item] = inventario.get(item, 0) + 1
    return inventario


def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente.
    """
    for item in items:
        inventario[item] = inventario.get(item, 0) + 1
    return inventario


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada item en la lista.
    """
    for item in items:
        if item in inventario:
            if inventario[item] > 0:
                inventario[item] -= 1
    return inventario


def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo.
    """
    if item in inventario:
        del inventario[item]
    return inventario


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con cantidad > 0.
    """
    resultado = []
    for item, cantidad in inventario.items():
        if cantidad > 0:
            resultado.append((item, cantidad))
    return resultado


def find_max_value(diccionario):
    """
    Retorna el nombre con el puntaje más alto.
    """
    if not diccionario:
        return ""
    max_nombre = None
    max_valor = float('-inf')
    for nombre, valor in diccionario.items():
        if valor > max_valor:
            max_valor = valor
            max_nombre = nombre
    return max_nombre


def reverse_dict(diccionario):
    """
    Invierte un diccionario: los valores pasan a ser claves.
    """
    invertido = {}
    for clave, valor in diccionario.items():
        if valor in invertido:
            invertido[valor] += str(clave)
        else:
            invertido[valor] = str(clave)
    return invertido


def word_frequency(palabras):
    """
    Retorna la frecuencia de cada palabra.
    """
    if not palabras:
        return {}
    frecuencia = {}
    for p in palabras:
        frecuencia[p] = frecuencia.get(p, 0) + 1
    return frecuencia


def find_biggest_expense(gastos):
    """
    Retorna la categoría con el promedio de gastos más alto.
    """
    if not gastos:
        return ""
    max_cat = ""
    max_promedio = -1
    for categoria, montos in gastos.items():
        promedio = sum(montos) / len(montos) if montos else 0
        if promedio > max_promedio:
            max_promedio = promedio
            max_cat = categoria
    return max_cat


def sum_expenses(gastos):
    """
    Retorna la suma total de los gastos por categoría.
    """
    resultado = {}
    for categoria, montos in gastos.items():
        resultado[categoria] = sum(montos)
    return resultado


def sum_expenses_by_type(gastos):
    """
    Suma montos agrupada por tipo (no por categoría).
    """
    por_tipo = {}
    for lista in gastos.values():
        for tipo, monto in lista:
            por_tipo[tipo] = por_tipo.get(tipo, 0) + monto
    return por_tipo