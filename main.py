from view import *

def main():
    while True:
        print('\nПривет! Это функционал CRUD, вот небольшие инструкции -  :)\n \n0: Выйти из интерфейса\n1: Получить все продукты\n2: Получить определенный продукт\n3: Создать продукт\n4: Обновить  продукт\n5: Удалить продукт')
        method = input('\nВведите метод:\t')

        if method == '0':
            print('\nСпасибо что пользуетесь моей продукцией!  😁\n')
            return''
        if method == '1':
            print(get_product())
            print('\n')
        if method == '2':
            id = int(input('Введите id:\t'))
            print(get_one_product(id))
            print('\n')
        if method == '3':
            print(get_post())
            print('\n')
        if method == '4':
            id = int(input('\nВведите id:\t'))
            print(get_update(id))
            print('\n')
        if method == '5':
            id = int(input('Введите id:\t\n'))
            print(get_delete(id))
            print('\n')
        else:
            print('Введена не существующая опция!  😐\n')

if __name__ == '__main__':
    main()