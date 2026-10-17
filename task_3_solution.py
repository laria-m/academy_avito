orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

# на какую сумму оформили возвраты
returned_sum = sum(order["amount"] for order in orders if order["status"] == "returned")
print(f"Общая сумма возвратов: {returned_sum}")
# кто хотя бы раз вернул заказ
returned_names = [order["buyer"] for order in orders if order["status"] == "returned"]
print('Хотя бы раз вернули заказ:')
for name in returned_names:
    print(name)
# сколько заказов доставлено покупателю
cnt_delivered  = len([order["id"] for order in orders if order["status"] == "delivered"])
print(f'{cnt_delivered} заказа доставлено')
# средний чек доставленных заказов
sum_delivered = sum(order["id"] for order in orders if order["status"] == "delivered")
avg_check = round(sum_delivered/cnt_delivered, 2)
print(f'Средний чек доставленных заказов: {avg_check}')