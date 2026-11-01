def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}
  
    # что можно забрать в любом из двух городов
    common_products = moscow & kazan
    print(common_products)
      
    # что есть только в Москве
    only_moscow = moscow - kazan
    print(only_moscow)
      
    # что есть только в Казани
    only_kazan = kazan - moscow
    print(only_kazan)
    
    # сколько разных товаров на обоих складах вместе
    all_products = moscow | kazan
    print(len(all_products))


if __name__ == '__main__':
    main()
