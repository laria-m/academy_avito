reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]
# Нужно найти:

# среднюю оценку каждого товара
ratings = {}
for review in reviews:
    product = review["product"].capitalize()
    if product not in ratings:
        ratings[product] = []
    ratings[product].append(review["stars"])
avg_ratings = {product: sum(stars) / len(stars) for product, stars in ratings.items()}
print('Средняя оценка кажого товара:')
for k,v in avg_ratings.items():
    print(f'{k}:{v}')
# худший товар по средней оценке среди тех, у кого хотя бы два отзыва
needed_goods = {product: stars for product, stars in ratings.items() if len(ratings[product])>=2}
avg_needed_goods = {product: sum(stars) / len(stars) for product, stars in needed_goods.items()}
worst_good = [product for product in avg_needed_goods if avg_needed_goods[product] == min(avg_needed_goods.values())]
print(f'Худший товар по средней оценке среди тех, у кого хотя бы два отзыва: {worst_good}')
# сколько отзывов на 1 или 2 звезды
low_cnt = len([review['id'] for review in reviews if review["stars"] <= 2])
print(f"Отзывов на 1 или 2 звезды: {low_cnt}")
# какую долю всех отзывов они составляют
all_cnt = len([review['id'] for review in reviews])
share = round(low_cnt/all_cnt, 2)
print(f'Их доля от всех отзывов: {share}')