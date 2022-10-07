# import datetime
from datetime import datetime
from os import getegid
now = datetime.now()
import json
FILE_PATH = 'data.json'


def get_product(ge_price = None, le_price = None, status_stock = None, status_out = None):
    with open(FILE_PATH, encoding = 'utf-8') as file:
        data = json.load(file)

        if ge_price:
            ge_price_start = 500
            ge_data = [i for i in data if i['price'] >= ge_price_start]
            return ge_data
        if le_price:
            le_price_start = 499
            le_data = [i for i in data if i['price'] <= le_price_start]
            return le_data
        if status_stock:
            status_in_stock = [i for i in data if i['status'] == 'в наличии']
            return status_in_stock
        if status_out:
            out_of_stock = [i for i in data if i['status'] == 'нет в наличии']
            return out_of_stock
        return data




def get_one_product(id):
    data = get_product()
    one_data = [i for i in data if i['id'] == id]
    
    if one_data:
        return one_data
    return'\nТакого товара не существует\n'




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




# print(get_post())
# print(get_product())
# print(get_one_product(1))
# print(get_update(1))
print(get_delete(1))