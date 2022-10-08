data = [
    {
        'id': 0,
        'name': 'none',
        'price': '120000'
    }
]

def get_product():
    filter_input = input('\nнажмите "enter" чтобы вывести все товары или выберите способ сортировки: цена(ц), статус(с), дата(д)\n\nВаша опция - \t').lower()  

    if filter_input == '':
        print('\n')
        return data
    if filter_input == 'ц':
        filter_price = int(input('Введите цену:\t'))
        cost = input('Хотите вывести продукт дороже указанной цены (да/нет)?\nВаш ответ:\t').lower
            
        if cost == 'да':
            ls = []
            for i in data:
                if i['price'] >= filter_price:
                    ls.append(i)
                    return ls
        elif cost == 'нет':
            for i in data:
                if i['price'] <= filter_price:
                    ls.append(i)


print(get_product())