# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

n = int(input('Введите число и нажмите Enter '))
def ListEl(n):
    list = [round((1+1/i)**i, 20) for i in range(1, n+1)]
    # for i in range(1, n+1):
    #     list.append(round((1+1/i)**i, 20))
    return list
print(f'{ListEl(n)} \nСумма элементов = {round(sum(ListEl(n)))}')
# print(f'Сумма элементов = {round(sum(ListEl(n)))}')
