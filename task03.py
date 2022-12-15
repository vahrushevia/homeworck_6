# 4'. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0


import random


def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)


create_list = lambda k: [random.randint(0, 10) for i in range(k+1)]


def create_str_file(kof):
    list = kof[::-1]
    st = ''
    if len(list) < 1:
        st = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                st += f'{list[i]}x**{len(list)-i-1}'
                if list[i+1] != 0:
                    st += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                st += f'{list[i]}x'
                if list[i+1] != 0:
                    st += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                st += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                st += ' = 0'
    return st


k = int(input("Введите натуральную степень k = "))
ko = create_list(k)
write_file(create_str_file(ko))
