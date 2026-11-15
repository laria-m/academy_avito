def add_attribute(data, field, func):
    """Добавляет в каждый словарь новое поле, вычисленное с помощью переданной функции"""
    for dictionary in data:
        dictionary[field] = func(dictionary)
    return data

