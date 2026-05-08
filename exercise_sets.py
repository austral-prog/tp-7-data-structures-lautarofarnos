# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    """
    Elimina los ingredientes duplicados de una receta.
    """
    return (nombre_plato, set(ingredientes))


def check_drinks(nombre_bebida, ingredientes):
    """
    Clasifica una bebida como "Cocktail" o "Mocktail".
    """
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"


def unique_chars(texto):
    """
    Retorna un set con los caracteres únicos de un string.
    """
    return set(texto)


def sum_set(numeros):
    """
    Recorre un set de números y retorna la suma total.
    """
    total = 0
    for n in numeros:
        total += n
    return total


def common_elements(set_a, set_b):
    """
    Retorna un nuevo set con los elementos que aparecen en AMBOS sets.
    """
    comunes = set()
    for elemento in set_a:
        if elemento in set_b:
            comunes.add(elemento)
    return comunes