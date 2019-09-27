# Дан одномерный массив и действительное число.
# Вставить данное число после всех максимальных элементов массива.
#
# Кондрашова
#
# a - основной список
# ch, ch1, ch2 - списки, по которым сравниваются все элементы
# i, y -  индексы
# l - проверка все ли элементы были числами
# c - указывает на то, к какому массиву ch, ch1 или ch2 принадлежит элемент
# x - действительное число
# mx - максимальный элемент массива

a = list(map(list, input('Введите данные массива через пробел: ').split()))
ch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ch1 = ['-', '+']
ch2 = ['.']
l = 0
print()

for i in range(0, len(a)):
    c = 0
    for y in range (0, len(a[i])):
        if y == 0:
            if a[i][y] in ch1:
                c = 1
            elif a[i][y] in ch:
                c = 2
            else:
                c = 5
                break
            
        elif c == 1:
            if not a[i][y] in ch:
                c = 5
                break
            else:
                c = 2
                
        elif c == 2:
            if a[i][y] in ch:
                c = 2
            elif a[i][y] in ch2:
                c = 3
            else:
                c = 5
                break

        elif c == 3 or c == 4:
            if not a[i][y] in ch:
                c = 5
                break
            else:
                c = 4

    if c == 5 or c == 1 or c == 3:
        l = 1
    if c != 5 and c != 1 and c != 3:
        for k in range(1, len(a[i])):
            a[i][0] += a[i][k]
        a[i][0] = float(a[i][0])

x = float(input('Введите действительное число: '))

if l == 0:
    s = [a[i][0] for i in range(0, len(a))]
    mx = s[0]
    mxi = 0
    for j in range(0, len(s)):
        if s[j] >= mx:
            mx = s[j]
    for i in range (0, len(s)):
        if s[i] == mx:
            print(s[i],'\n', x, sep = '')
        else:
            print(s[i])
                 
else:
    print('Некорректные данные')
