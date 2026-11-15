def count_missing(data):
    """Подсчитывает количество пропущенных значений по каждому полю списка словарей"""
    result = {}
    for dictionary in data:
        for field in dictionary:
            if field not in result:
                result[field] = 0

    for dictionary in data:
        for field in result:
            if dictionary.get(field) is None:
                result[field]+=1
            
    return result


def top_n(groups, n=5):
    """Возвращает n групп с наибольшим количеством элементов"""
    return sorted(
        groups.items(),
        key=lambda item: len(item[1]),
        reverse=True
    )[:n]       


def calculate_mean(values):
    """Вычисляет среднее арифметическое списка чисел"""
    return sum(values) / len(values)


def calculate_median(values):
    """Вычисляет медиану списка чисел"""
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2


def calculate_mode(values):
    """Находит наиболее часто встречающееся значение в списке (моду)"""
    mode = values[0]
    max_count = 0
    for value in values:
        count = values.count(value)
        if count > max_count:
            max_count = count
            mode = value
    return mode

        
    