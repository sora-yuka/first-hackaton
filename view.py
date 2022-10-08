from datetime import datetime
from os import getegid
now = datetime.now()
import json
FILE_PATH = 'data.json'

# Фильтрация по цене

def get_product(filter = None):
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)

    filter_input = input('\nнажмите "enter" чтобы вывести все товары или выберите способ сортировки: цена(ц), статус(с), дата(д)\n\nВаша опция - \t').lower()  

    if filter_input == '':
        print('\n')
        return data
    if filter_input == 'ц':
        filter_price = int(input('Введите цену:\t'))
        cost = input('Хотите вывести продукт дороже указанной цены (да/нет)?\nВаш ответ:\t').lower()
            
        if cost == 'да':
            ge_data = [i for i in data if int(i['price']) >= filter_price]
            if ge_data:
                return ge_data
            return'\nТакого продукта не существует\n'
        elif cost == 'нет':
            le_data = [i for i in data if int(i['price']) <= filter_price]
            if le_data:
                return le_data
            return'\nТакого товара не существует\n'

       

    
    


# Фильтрация по статусу    


    if filter_input == 'с':
        filter_status = input('Хотите вывести продукты имеющиеся в наличии(да/нет)?\t\n\nВаш ответ:\t').lower()

        if filter_status == 'да':
            status_stock = [i for i in data if i['status'] == 'в наличии' or 'всегда в наличии']
            if status_stock:
                return  status_stock
            return'\nТакого товара не существует\n'
        if filter_status == 'нет':
            status_out = [i for i in data if i['status'] == 'нет в наличии']
            if status_out:
                return status_out
            return'\nТакого товара не существует\n'
        return data

    return('\nВведите правильную опцию\n')







def get_one_product(id):
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)
    one_data = [i for i in data if i['id'] == id]
    
    if one_data:
        print('\n')
        return one_data
    else:
        return'\nТакого продукта не существует'




def get_post():
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)
    maxid = max([i['id'] for i in data])

    data.append({
            'id': maxid + 1,
            'name': input('Введите название товара:\t'),
            'price': input('Введите цену:\t'),
            'created_at': str(now),
            'updated_at': str(now),
            'description': input('Введите описание товара:\t'),
            'status': 'в наличии'
        })

    with open(FILE_PATH, 'w+', encoding = 'utf-8') as file:
        json.dump(data, file)

    
    return'\nТовар успешно опубликован\n'




def get_update(id):
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)
    data_id = [i for i in data if i['id'] == id]

    if data_id:
        data_index = data.index(data_id[0])
        data[data_index]['name'] = input('Введите новое название:\t')
        data[data_index]['price'] = input('Введите новую цену:\t')
        data[data_index]['updated_at'] = str(now)
        data[data_index]['description'] = input('Введите новое описание:\t')
        data[data_index]['status'] = input('в наличии/нет в наличии:\t').lower()

        json.dump(data, open(FILE_PATH, 'w'))
        return'\nОбновлено успешно\n'
    return'Такого продукта не существует'


def get_delete(id):
    with open(FILE_PATH, encoding='utf-8') as file:
        data = json.load(file)
    delete_id = [i for i in data if i['id'] == id]

    if delete_id:
        data.remove(delete_id[0])
        json.dump(data, open(FILE_PATH, 'w'))

        return'\nУспешно удалено\n'
    
    return'\nТакого товара не существует\n'



ls = ['1', '2', '3', '4', '5']