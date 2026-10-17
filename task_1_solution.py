moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

# что можно забрать в любом из двух городов
any = moscow | kazan
print(any)

# что есть только в Москве
only_moscow = moscow - kazan
print(only_moscow)

# что есть только в Казани
only_kazan = kazan - moscow
print(only_kazan)

# сколько разных товаров на обоих складах вместе
each = moscow & kazan
print(each)