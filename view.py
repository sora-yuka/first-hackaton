from datetime import datetime
from os import getegid
now = datetime.now()
import json
FILE_PATH = 'data.json'


def get_product(filter = None):
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)


    filter = str(input('\nнажмите "enter" чтобы вывести все товары или выберите способ сортировки: цена(ц), статус(с), дата(д)\nВаша опция - \t')).lower()  

    if filter == '':
        print('\n')
        return data
    if filter == 'ц':
        filter_price = int(input('Введите цену:\t'))
        cost = input(f'Хотите вывести продукт дороже {filter_price} (да/нет)?\t').lower
            
        if cost == 'y':
            data = [i for i in data if i['price'] >= filter_price]
            if data:
                return data
            return'\nТакого продукта не существует\n'
        elif cost == 'n':
            data = [i for i in data if i['price'] <= filter_price]
            if data:
                return data
            return'\nТакого товара не существует\n'

       

    
    
    # return data

# Фильтрация по статусу    


    if filter == 'с':
        filter_status = input('Хотите вывести все продукты имеющиеся в наличии(да/нет)?    ').lower()

        if filter_status == 'да':
            status_stock = [i for i in data if i['status'] == 'в наличии']
            if status_stock:
                return  status_stock
            return'\nТакого товара не существует\n'
        if filter_status == 'нет':
            status_out = [i for i in data if i['status'] == 'нет в наличии']
            if status_out:
                return status_out
            return'\nТакого товара не существует\n'
        return data

    if filter == 'д':
        pass
    else:
        return('\nВведите правильную опцию\n')







def get_one_product(id):
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)
    one_data = [i for i in data if i['id'] == id]
    
    if one_data:
        print('\n')
        return one_data
    else:
        return'Такого продукта не существует'




def get_post():
    data = get_product()
    maxid = max([i['id'] for i in data])

    data.append({
            'id': maxid + 1,
            'name': input('Введите название товара:   '),
            'price': input('Введите цену:   '),
            'created_at': str(now),
            'updated_at': str(now),
            'description': input('Введите описание товара:    '),
            'status': 'в наличии'
        })

    with open(FILE_PATH, 'w+', encoding = 'utf-8') as file:
        json.dump(data, file)

    
    return'\nТовар успешно опубликован\n'




def get_update(id):
    data = get_product()
    data_id = [i for i in data if i['id'] == id]

    if data_id:
        data_index = data.index(data_id[0])
        data[data_index]['name'] = input('Введите новое название:    ')
        data[data_index]['price'] = input('Введите новую цену:    ')
        data[data_index]['updated_at'] = str(now)
        data[data_index]['description'] = input('Введите новое описание:    ')
        data[data_index]['status'] = input('в наличии/нет в наличии:    ')

        json.dump(data, open(FILE_PATH, 'w'))
        
        return'\nОбновлено успешно\n'




def get_delete(id):
    data = get_product()
    delete_id = [i for i in data if i['id'] == id]

    if delete_id:
        # data_index = delete_id.index(delete_id[0])
        data.remove(delete_id[0])
        # data[data_index]['status'] = 'нет в наличии'
        json.dump(data, open(FILE_PATH, 'w'))

        return'\nУспешно удалено\n'
    
    return'\nТакого товара не существует\n'
