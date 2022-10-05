import sys

ent_list = input('Введите последовательность чисел через пробел') # Вводим последовательность
ent_num = input('Введите любое число') # Вводим число

num = int(ent_num)
N = [] # Список

check_list = ent_list.replace(' ', '') # Убираем пробелы

if not check_list.isdigit() or not ent_num.isdigit(): # Проверяем введены ли цифры
    print('Введены неверные данные')
    sys.exit()

num_list = list(map(int, ent_list.split())) # Меняем строку на список

for i in range(len(num_list)):
    for j in range(len(num_list)-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

def binary_search(num_list, num, left, right):
    if left > right:
        return False


    middle = (right + left) // 2
    if num_list[middle] == num:
        return middle
    elif num < num_list[middle]:
        return binary_search(num_list, num, left, middle - 1)
    else:
        return binary_search(num_list, num, middle +1, right)

print()
print()
print(f'Введенная последовательность чисел: {num_list}')
print(f'Введенное число: {num}')


if num not in num_list:
    print(f'Числа {num} нет в списке')

elif  binary_search(num_list, num, 0, len(num_list)) - 1 < 0:
    print(f'Позиция числа: {binary_search(num_list, num, 0, len(num_list))}')
    print(f'В последовательности нет числа меньше {num_list[binary_search(num_list, num, 0, len(num_list) - 1)]}')
    print(f'Номер позиции элемента большего или равного введенному числу = {binary_search(num_list, num, 0, len(num_list) - 1)}')
    print(f'Элемент = {num_list[binary_search(num_list, num, 0, len(num_list) - 1)]}')


else:
    print(f'Позиция числа: {binary_search(num_list, num, 0, len(num_list))}')
    print(f'Номер позиции элемента меньше введенного числа = {binary_search(num_list, num, 0, len(num_list)) - 1}')
    print(f'Элемент = {num_list[binary_search(num_list, num, 0, len(num_list)) - 1]}')
    print(f'Номер позиции элемента большего или равного введенному числу = {binary_search(num_list, num, 0, len(num_list) - 1)}')
    print(f'Элемент = {num_list[binary_search(num_list, num, 0, len(num_list) - 1)]}')
