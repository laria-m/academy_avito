from json_dict_processing import create_processor
from prizes_configs import prize_processor

def process_year(date):
    """Извлекает год из строки с датой, возвращая None при отсутствии даты"""
    if date is None:
        return None
    return int(date[:4])


def person_processor():
    """Создаёт функцию обработки данных лауреата-физического лица по заданной конфигурации"""
    return create_processor(CONFIG_PERSON)


def org_processor():
    """Создаёт функцию обработки данных организации-лауреата по заданной конфигурации"""
    return create_processor(CONFIG_ORG)


def process_persons(person):
    """Преобразует исходные данные лауреата-физического лица в словарь с выбранными полями"""
    processor = person_processor()
    return processor(person)


def process_orgs(org):
    """Преобразует исходные данные организации-лауреата в словарь с выбранными полями"""
    processor = org_processor()
    return processor(org)


CONFIG_PERSON = {
    "id": ["id"],
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor())
}


CONFIG_ORG = {
    "id": ["id"],
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor())
}

