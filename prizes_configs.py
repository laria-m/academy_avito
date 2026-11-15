from json_dict_processing import create_processor

CONFIG_PRIZE = {
    "prize_amount": ["prizeAmount"],
    "prize_amount_adjusted": ["prizeAmountAdjusted"],
    "award_year": (["awardYear"], int),
    "category_en": ["category", "en"],
    "prize_status": ["prizeStatus"]
}


def prize_processor():
    """Создаёт функцию обработки списка Нобелевских премий по заданной конфигурации"""
    return create_processor(CONFIG_PRIZE, list_processor=True)