# Требуется найти определитель матрицы.
# Протестировать на матрицу из одних единиц.
#
# Кондрашова
#
# det - определитель матрицы
# n - порядок матрицы
# k - проверка на матрицу, состоящую из одних единиц

n = int(input('Введите порядок матрицы: '))
a = []
a = [(list(map(list, input('Введите строку: ').split())))for i in range(n)]

ch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ch1 = ['-', '+']
ch2 = ['.']
l = 0
print()

for i in range(0, len(a)):
    c = 0
    for j in range(0, len(a[i])):
        for y in range(0, len(a[i][j])):
            if y == 0:
                if a[i][j][y] in ch1:
                    c = 1
                elif a[i][j][y] in ch:
                    c = 2
                else:
                    c = 5
                    break
            
            elif c == 1:
                if not a[i][j][y] in ch:
                    c = 5
                    break
                else:
                    c = 2
                
            elif c == 2:
                if a[i][j][y] in ch:
                    c = 2
                elif a[i][j][y] in ch2:
                    c = 3
                else:
                    c = 5
                    break

            elif c == 3 or c == 4:
                if not a[i][j][y] in ch:
                    c = 5
                    break
                else:
                    c = 4

        if c == 5 or c == 1 or c == 3:
            l = 1
        if c != 5 and c != 1 and c != 3:
            for k in range(1, len(a[i][j])):
                a[i][j][0] += a[i][j][k]
            a[i][j] = float(a[i][j][0])          

if l == 0:
    k = 0

    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                k = 1
                break
    if k == 0:
        print('Матрица состоит из одних единиц.\n',
              'Определитель = 0', sep = '')
    else:
        if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
            print('Определитель матрицы: 0')
        elif a[0][0] == a[0][1] and a[2][0] == a[2][1] and a[1][0] == a[1][1]\
             or a[0][0] == a[0][2] and a[2][0] == a[2][2] and a[1][0]==a[1][2]\
             or a[0][1] == a[0][2] and a[2][1] == a[2][2] and a[1][1] == a[1][2]:
            print('Определитель матрицы: 0')
        else:
            s = 1
            t = -1
            while t < n - 1:
                t += 1
                x = a[t][t]
                if x != 0:
                    s *= x
                    for i in range(n):
                        a[t][i] = a[t][i] / x

                for i in range(t + 1, n):
                    y = a[i][t]
                    for j in range(n):
                        a[i][j] = a[i][j] - a[t][j] * y
         
            det = a[n - 1][n - 1] * s
            print('Определитель матрицы: {:.5f}'.format(det))

else:
    print('Некорректные данные')
