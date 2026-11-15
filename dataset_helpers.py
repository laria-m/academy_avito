def group_by(data, field):
    """Группирует список словарей по значениям указанного поля"""
    result = {}
    for dictionary in data:
        value = dictionary.get(field)
        if value not in result:
            result[value] = []
        result[value].append(dictionary)
    return result