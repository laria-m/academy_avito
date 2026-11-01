def main():
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
    for query, cnt in queries_cnt.items():
        if cnt == 1:
            print(f"Запрос {query} ввели {cnt} раз")
        else:
            print(f"Запрос {query} ввели {cnt} раза")
    # какой запрос вводили чаще всего
    max_count = max(queries_cnt.values())
    for query, cnt in queries_cnt.items():
        if cnt == max_count:
            print(f"Запрос, который выводили чаще всего: {query}")
    # какую долю всех поисков он занимает
    share = round(max_count / len(queries), 2)
    print(f"Доля от всех поисков: {share}")
    # какие запросы встретились один раз
    print("Запросы, которые встретились один раз:")
    for query, cnt in queries_cnt.items():
        if cnt == 1:
            print(query)


if __name__ == '__main__':
    main()
