days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

# выручка за всю неделю
weekly_revenue = sum(day['revenue'] for day in days)
print(f'Выручка за неделю: {weekly_revenue}')
# день с самой большой выручкой
max_revenue = max([day['revenue'] for day in days])
max_revenue_day = [day['day'] for day in days if day['revenue'] == max_revenue]
print(f'День с самой большой выручкой: {max_revenue_day}')
# средняя выручка на один заказ в каждый день
avg_revenue = {day["day"]: day["revenue"] / day["orders"] for day in days}
print('Средняя выручка на заказ по дням:')
for k,v in avg_revenue.items():
    print(f'{k}: {v}')
# дни, где возвратов больше 20% заказов
many_returns_days = [day['day'] for day in days if day['returns']/day['orders'] > 0.2]
print('Дни, где возвратов больше 20%:')
for day in many_returns_days:
    print(day)