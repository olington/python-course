import os
import pickle
from pathlib import Path

direct = '/C:/Users/olga/Documents/BMSTU/bd/lib1'
extension = '.bin'

col = ('login', 'hash', 'session', 'ban')


def create_file(path):
    open(path, 'w+').close()

def try_choose_database():
    print('Выберите базу данных:\n')
    list_existing_databases()
    db = construct_db_path(input())
    if db_exists(db):
        return db
    return None

def construct_db_path(name):
    return direct + name + extension

def list_existing_databases():
    files = []
    for file in os.listdir(direct):
        if file.endswith(extension):
            files.append(file[:-4])
    print(', '.join(files))
    print()

def db_exists(db):
    if not Path(db).is_file():
        return False
    return True

while True:
    print('Выберите действие:\n')
    print('1. Создать новую базу данных.')
    print('2. Открыть существующую базу данных.')
    
    k = input('Введите номер команды: ')
    print()

    if k == '1':
        db_name = input('Введите название базы данных: ')
        db = construct_db_path(db_name)
        if db_exists(db):
            print('База данных с таким названием уже существует.\n')
        else:
            create_file(construct_db_path(db_name))
            print(f'Создана база данных {db_name}.\n')

    elif k == '2':
        db = try_choose_database()
        if db is None:
            print('Выбранная база данных не существует.\n')

def display_db_menu(db):
    choices = ('1', '2', '3', '4', '5')

    while True:
        print('Выберите действие:\n')
        print('1) Добавить новую запись в базу данных')
        print('2) Вывести информацию из базы данных')
        print('3) Поиск по базе данных')
        print('4) Удаление из базы данных')
        print('5) Закрыть базу данных')

        choice = input()
        if choice in choices:
            break
        print('Несуществующий пункт меню.\n')

    if choice == '1':
        add_db_entry(db)
    elif choice == '2':
        print_db_contents(db)
    elif choice == '3':
        min = checked_input('Нижняя граница включительно: ', int)
        max = checked_input('Верхняя граница включительно: ', int, lambda x: min <= x)
        search_db_contents(db, min, max)
    elif choice == '4':
        min = checked_input('Нижняя граница включительно: ', int)
        max = checked_input('Верхняя граница включительно: ', int, lambda x: min <= x)
        delete_db_contents(db, min, max)
    elif choice == '5':
        display_main_menu()

    display_db_menu(db)
    

def add_db_entry(db):
    with open(db, 'rb+') as f:
        if is_empty(db):
            index = '0'
            data = {}
        else:
            data = pickle.load(f)
            if len(data) == 0:
                index = str(len(data))
            else:
                index = max(int(key) for key, _ in data.items()) + 1

        data[index] = {}
        for field in col:
            data[index][field] = input(f'{field}: ')

    with open(db, 'wb') as f:
        pickle.dump(data, f)


def print_db_contents(db):
    with open(db, 'rb') as f:
        if is_empty(db):
            print()
            return

        data = pickle.load(f)
        for _, item in data.items():
            row = ''
            for field in FIELDS:
                row += f'{field}:\t{item[field]}\t'
            print(row)


def is_empty(file):
    return os.stat(file).st_size == 0


def search_db_contents(db, min, max):
    with open(db, 'rb') as f:
        data = pickle.load(f)
        for key, _ in data.items():
            if min <= int(key) <= max:
                print(data[key])


def delete_db_contents(db, min, max):
    f = open(db, 'rb')
    data = pickle.load(f)
    keys_to_delete = []
    for key, _ in data.items():
        if min <= int(key) <= max:
            keys_to_delete.append(key)

    if len(keys_to_delete) > 0:
        for k in keys_to_delete:
            data.pop(k, None)
    f.close()

    with open(db, 'wb') as f:
        pickle.dump(data, f)

    print(f'Удалено {len(keys_to_delete)} строк.\n')
  
    
    
