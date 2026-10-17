queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

# сколько всего поисковых запросов в ленте
print(f"Всего поисковых запросов в ленте: {len(queries)}")
# сколько раз ввели каждый запрос
queries_cnt = {}
for query in queries:
    if query not in queries_cnt:
        queries_cnt[query] = 1
    else:
        queries_cnt[query] += 1
for k,v in queries_cnt.items():
    if v == 1:
        print(f"Запрос {k} вели {v} раз")
    else:
        print(f"Запрос {k} вели {v} раза")
# какой запрос вводили чаще всего
max_count = max(queries_cnt.values())
for k, v in queries_cnt.items():
    if v == max_count:
        print(f"Запрос, который выводили чаще всего: {k}")
# какую долю всех поисков он занимает
share = round(queries_cnt["iphone"] / len(queries),2)
print(f"Доля от всех поисков: {share}")
# какие запросы встретились один раз
print("Запросы, которые встретились один раз:")
for k, v in queries_cnt.items():
    if v == 1:
        print(k)
