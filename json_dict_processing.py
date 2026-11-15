def extract_nested_value(obj, keys):
    """Извлекает значение из вложенного словаря по последовательности ключей"""
    item = obj
    for k in keys:
        if not isinstance(item, dict):
            return None     
        item = item.get(k)
    return item 


def process_dictionary_with_config(dictionary, config):
    """Преобразует словарь по конфигурации, извлекая и обрабатывая нужные поля"""
    result = {}
    for field, keys in config.items():
        if isinstance(keys, tuple):
            value = extract_nested_value(dictionary, keys[0])
            value = keys[1](value)
        else:
            value = extract_nested_value(dictionary, keys)
        result[field] = value
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """Применяет заданную конфигурацию обработки к каждому словарю в списке"""
    result = []
    for dictionary in list_of_dicts:
        processed_dictionary = process_dictionary_with_config(dictionary, config)
        result.append(processed_dictionary)
    return result


def create_processor(config, list_processor=False):
    """Создаёт функцию обработки одного словаря или списка словарей по конфигурации"""
    def processor(dictionary):
        if list_processor:
            return process_list_of_dicts_with_config(dictionary, config)
        else:
            return process_dictionary_with_config(dictionary, config)
    return processor
    
        