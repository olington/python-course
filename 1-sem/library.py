lib = [{'Название':'Отверженные','Автор':'Гюго','Страна':'Франция','Год':'1862'},
       {'Название':'Война и мир','Автор':'Толстой','Страна':'Россия','Год':'1867'},
       {'Название':'Холодный дом','Автор':'Диккенс','Страна':'Англия','Год':'1853'},
       {'Название':'Три товарища','Автор':'Ремарк','Страна':'Германия','Год':'1936'},
       {'Название':'Остров','Автор':'Хаксли','Страна':'Англия','Год':'1962'}]

n = 'Название'
t = 'Автор'
c = 'Страна'
z = 'Год'
r = 'Некорректные данные'

def dig(q):
    if q.isdigit() is False:
        return False
    else:
        return True

def abc(q):
    if q.isalpha() is False:
        return False
    else:
        return True

def abc1(q):
    if q.isalnum() is False:
        return False
    else:
        return True

import pickle

lenlib = len(lib)
x = open('lib.txt', 'wb')
for i in lib:
    pickle.dump(i, x)
x.close()

x = open('lib.txt', 'rb')

rg = {'lib.txt':lenlib}

def new_bd():
    k = '1'
    global x
    global jj
    x.close()
    j = 0
    name = input('Введите название базы данных: ')
    x = open(name+'.txt', 'wb')
    while k != '2':
        a = {}
        a[n] = input(n + ': ')
        if abc1(a[n]) is False:
            print(r)
            continue
        a[c] = input(c + ': ')
        if abc(a[c]) is False:
            print(r)
            continue
        a[t] = input(t + ': ')
        if abc(a[t]) is False:
            print(r)
            continue 
        a[z] = input(z + ': ')
        if dig(a[z]) is False:
            print(r)
            continue        
        pickle.dump(a, x)
        j += 1
        print('1 - добавить еще запись,\n2 - не добавлять больше записей')
        k = input('Введите команду: ')
    rg[name + '.txt'] = j
    print('\nДобавлена новая база данных\n',
    'Название: ', name, sep = '')
    print()
    x.close()
    x = open(name+'.txt', 'rb')

s = 'lib.txt'
def exist_bd():
    global s
    s1 = input('Введите название файла, который необходимо открыть: ')
    s1 += '.txt'
    global x
    s = s1
    x = open(s, 'rb')
    k = 0
    while True:
        try:
            a1 = pickle.load(x)
            k += 1
        except EOFError:
            break
    rg[s] = k

def output():
    global x
    global s
    global rg
    print(s)
    print(rg)
    x = open(s, 'rb')
    print('{:15}'.format(n),\
          '{:15}'.format(t),\
          '{:15}'.format(c),\
          '{:15}'.format(z), sep = ' ', end = '\n')
    for i in range(rg[s]):
        q = pickle.load(x)
        print('{:15}'.format(q[n]),\
              '{:15}'.format(q[t]),\
              '{:15}'.format(q[c]),\
              '{:15}'.format(q[z]), sep = ' ', end = '\n')

def new_entry():
    global x
    global s
    x = open(s, 'ab')
    a = {}
    a[n] = input(n+': ').split()
    for i in range(len(a[n])):
        if abc1(a[n][i]) is False:
            print(r)
            return r
    a[n] = ' '.join(a[n])
    a[t   ] = input(t + ': ').split()
    for i in range(len(a[c])):
        if abc(a[c][i]) is False:
            print(r)
            return r
    a[c] = ' '.join(a[c])
    a[c] = input(c+': ').split()
    for i in range(len(a[c])):
        if abc(a[c][i]) is False:
            print(r)
            return r
    a[c] = ' '.join(a[c])
    a[z] = input(z+': ')
    if dig(a[z]) is False:
        print('n'+r)
        return r
    pickle.dump(a, x)
    rg[s] += 1
    x.close()
    x = open(s, 'rb')

def filt():
    print('Выберите параметры фильтра:\n\
    1. Автор.\n\
    2. Год.\n\
    3. Автор и год.\n')
    k1 = input('Введите команду: ')
    if k1 == '1':
        filt_str()
    elif k1 == '2':
        filt_num()
    elif k1 == '3':
        filt_str_num()
    else:
        print('Несуществующая команда')

def filt_str():
    global x
    global s
    global rg
    v = input('Введите автора: ')
    if abc(v) is False:
        print(r)
        return r
    print()
    x = open(s, 'rb')
    print('{:15}'.format(n),\
          '{:15}'.format(t),\
          '{:15}'.format(c),\
          '{:15}'.format(z), sep = ' ', end = '\n')
    for i in range(rg[s]):
        a1 = pickle.load(x)
        if a1[t] == v:
            print('{:15}'.format(a1[n]),\
              '{:15}'.format(a1[t]),\
              '{:15}'.format(a1[c]),\
              '{:15}'.format(a1[z]), sep = ' ', end = '\n')
    x.close()

def filt_num():
    global x
    global s
    global rg
    v = input('Введите год: ')
    if dig(v) is False:
        print(r)
        return r
    print()
    print('{:15}'.format(n),\
          '{:15}'.format(c),\
          '{:15}'.format(t),\
          '{:15}'.format(z), sep = ' ', end = '\n')   
    x = open(s, 'rb')
    for i in range(rg[s]):
        a1 = pickle.load(x)
        if int(a1[z]) == int(v):
            print('{:15}'.format(a1[n]),\
              '{:15}'.format(a1[c]),\
              '{:15}'.format(a1[t]),\
              '{:15}'.format(a1[z]), sep = ' ', end = '\n')
    x.close()

def filt_str_num():
    global x
    global s
    global rg
    v1 = input('Введите автора: ')
    if abc(v1) is False:
        print(r)
        return r    
    v2 = input('Введите год: ')
    if dig(v2) is False:
        print(r)
        return r
    print()
    print('{:15}'.format(n),\
          '{:15}'.format(t),\
          '{:15}'.format(c),\
          '{:15}'.format(z), sep = ' ', end = '\n')    
    x = open(s, 'rb')
    for i in range(rg[s]):
        a1 = pickle.load(x)
        if a1[t] == v1 and int(a1[z]) == int(v2):
            print('{:15}'.format(a1[n]),\
              '{:15}'.format(a1[t]),\
              '{:15}'.format(a1[c]),\
              '{:15}'.format(a1[z]), sep = ' ', end = '\n')
    x.close()

def delete():
    global x
    global s
    global rg
    print(s)
    print(rg)
    x = open(s, 'rb')
    y = open('n.txt', 'wb')
    v = input('Введите название: ')
    k = 0
    for i in range(rg[s]):
        a1 = pickle.load(x)
        if a1[n] != v:
            pickle.dump(a1, y)
            k += 1
            print(a1)
            print(k)
    x.close()
    y.close()
    x = open(s, 'wb')
    y = open('n.txt', 'rb')
    for i in range(k):
        a1 = pickle.load(y)
        pickle.dump(a1, x)
    rg[s] = k
    
y = open('n.txt')
def save_bd():
    global x
    global s
    global rg
    global x1
    global y
    x.close()
    x = open(s, 'wb')
    
while True:
    print()
    print('1. Создать новую базу данных.\n',
          '2. Открыть существующую базу данных.\n',
          '3. Просмотреть все записи в базе данных.\n',
          '4. Добавить новую запись.\n',
          '5. Реализовать поиск элементов.\n',
          '6. Удаление записи.\n',
          '7. Сохранить фойл.\n',
          '8. Завершить работу.\n', sep = '', end = '\n')
    k = input('Введите команду: ')
    print()
    if k == '1':
        new_bd()
    elif k == '2':
        exist_bd()
    elif k == '3':
        output()
    elif k == '4':
        new_entry()
    elif k == '5':
        filt()
    elif k == '6':
        delete()
    elif k == '7':
        save_bd()
    elif k == '8':
        x.close()
        break
    else:
        print('\n' + r)
