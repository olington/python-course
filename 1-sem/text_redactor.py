t = ['На краю дороги стоял дуб. Он был, вероятно, в десять раз старше берез, ',
     'составлявших лес, в десять раз толще и в два раза выше каждой березы. ',
     'Это был огромный, в два обхвата дуб, с обломанными суками и корой, ',
     'заросшей старыми болячками. С огромными, неуклюже, несимметрично ',
     'растопыренными корявыми руками и пальцами, он старым, сердитым и ',
     'презрительным уродом стоял между улыбающимися березами. Только он один ',
     'не хотел подчиниться обаянию весны и не хотел видеть ни весны, ни солнца. ']
for i in range(len(t)):
    print(t[i])
print()
        
while True:
    print('1. Удаление слова.\n',
      '2. Замена слова.\n',
      '3. Выравнивание текста по левому краю.\n',
      '4. Выравнивание текста по ширине.\n',
      '5. Выравнивание текста по правому краю.\n',
      '6. Отсортировать слова в самом длинном по числу символов предложении.\n',
      '7. Завершение работы.',sep = '')
    print()
    
    k = input('Введите команду: ')
    print()
    
    if k == '1':
        a = input('Введите слово, которое будет удалено: ')
        a.strip()
        print()
        for i in a:
            if i == ' ':
                a = input('Введите одно слово: ')
                print()
        a2 = a.lower()
        a3 = a[0].upper() + a[1:]
        a1 = a + ' '
        a2 = a2 + ' '
        a3 = a3 + ' '
        a4 = a + '.'.strip()
        a5 = a + ','.strip()
        a6 = a2.strip() + '.'
        a7 = a2.strip() + ','
        a8 = a3.strip() + '.'
        a9 = a3.strip() + ','
        for i in range(len(t)):
            t[i] = t[i].replace(a1, '')
            t[i] = t[i].replace(a2, '')
            t[i] = t[i].replace(a3, '')
            t[i] = t[i].replace(a4, '.')
            t[i] = t[i].replace(a5, ',')
            t[i] = t[i].replace(a6, '.')
            t[i] = t[i].replace(a7, ',')
            t[i] = t[i].replace(a8, '.')
            t[i] = t[i].replace(a9, ' ')
            print(t[i])
        print()

    elif k == '2':
        b = input('Введите слово, которое будет заменено: ')
        print()
        for i in b:
            if i == ' ':
                b = input('Введите одно слово: ')
                print()
   
        d = input('Введите слово, которое будет выведено вместо замененного: ')
        print()
        for j in d:
            if j == ' ':
                d = input('Введите одно слово: ')
                    
        print()
        print(b)
        b2 = b.lower()
        b3 = b[0].upper() + b[1:]
        b1 = ' ' + b + ' '
        b2 = ' ' + b2 + ' '
        b3 = b3 + ' '
        b4 = b.strip() + '.'
        b5 = b.strip() + ','
        b6 = b2.strip() + '.'
        b7 = b2.strip() + ','
        b8 = b3.strip() + '.'
        b9 = b3.strip() + ','
        for i in range(len(t)):
            t[i] = t[i].replace(b1, d+' ')
            t[i] = t[i].replace(b2, d+' ')
            t[i] = t[i].replace(b3, d+' ')
            t[i] = t[i].replace(b4, d+'.')
            t[i] = t[i].replace(b5, d+',')
            t[i] = t[i].replace(b6, d+'.')
            t[i] = t[i].replace(b7, d+',')
            t[i] = t[i].replace(b8, d+'.')
            t[i] = t[i].replace(b9, d+',')
            print(t[i])
        print()
            
    elif k == '3':
        for i in t:
            print('{:<73}'.format(i))
        print()
            
    elif k == '4':
        s = ''
        mn = []
        lenmax = 0
        for i in range(len(t)):
            m = []
            lm = len(t[i])
            if lm > lenmax:
                lenmax = int(lm)
            for j in range(len(t[i])):
                if t[i][j] != ' ':
                    s += t[i][j]
                else:
                    m.append(s)
                    s = ''
                    n = []
            mn.append(m)
            
        for i in range(len(mn)):
            q = ''
            if len(mn[i]) == 1:
                for j in mn[i]:
                    print(j, end = '')
            elif len(mn[i]) == 0:
                continue
            else:
                while len(q) < 73:
                    for j in range(len(mn[i])):
                        mn[i][j] += ' '
                        q = ''.join(mn[i])
                        q = q.strip()
                        if len(q) >= 73:
                            break
            print(q)            
        print()
        
    elif k == '5':
        for i in t:
            print('{:>74}'.format(i))
        print()

    elif k == '6':
        w = ''
        for i in range(len(t)):
            for j in range(len(t[i])):
                w += t[i][j]
                
        t1 = []
        h = ''
        for i in range(len(w)):
            if w[i] != '.':
                h += w[i]
            else:
                h += '.'
                t1.append(h)
                h = ''
                
        lmax = 0
        r = 0
        for i in range(len(t1)):
            if len(t1[i]) > lmax:
                lmax = len(t1[i])
                r = t1[i]
        r = r.strip()
        t2s = ''
        for y in r:
            t2s += y
        t2 = []
        v = ''
        for i in range(len(r)):
            if r[i] != ' ':
                if r[i] != '.' and r[i] != ',':
                    v += r[i]
            else:
                t2.append(v)
                v = ''
        t2.append(v)

        for i in range(len(t2) - 1):
            for j in range(len(t2) - 2, i - 1, -1):
                if len(t2[j]) > len(t2[j+1]):
                    t2[j], t2[j+1] = t2[j+1], t2[j]
        s3 = ''
        for i in t2:
            s3 = ' '.join(t2)
        s3 = s3.strip()
        
        print('Самое длинное по числу символов предложение:\n', t2s, sep = '')
        print()
        print('Отсортированное предложение:\n', s3, sep = '')
        print()
            
    elif k == '7':
        break
    
    else:
        print('Данная команда не существует.')
        print()
