# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Из многочлена убираю ненужные символы
def remove_char(pol):
    pol = pol.replace("+ ", "").replace(" = 0", "*x^0").replace("- ", "-")
    pol = list(pol.split())
    return pol

# Из списка делаю словарь, в котором степень будет ключем
def transformation_from_list_to_dict(pol):
    dict_pol = {}
    for i in range(len(pol)):
        pol[i] = pol[i].split('*x^')
        dict_pol[int(pol[i][1])] = int(pol[i][0])
    return dict_pol

file1 = 'file1.txt'
file2 = 'file2.txt'
file_sum = 'file_sum.txt'

with open(file1, 'r') as data:
    polynomial1 = data.readline()

with open(file2, 'r') as data:
    polynomial2 = data.readline()

print(polynomial1)  # 9*x^4 + 4*x^3 + 1*x^2 + 7*x^1 + 4 = 0
print(polynomial2)  # 10*x^3 - 3*x^2 + 9 = 0

pol1_no_symbols = remove_char(polynomial1)  # ['9*x^4', '4*x^3', '1*x^2', '7*x^1', '4*x^0']
pol2_no_symbols = remove_char(polynomial2)  # ['10*x^3', '-3*x^2', '9*x^0']

dict1_polynomial = transformation_from_list_to_dict(pol1_no_symbols)  # {4: 9, 3: 4, 2: 1, 1: 7, 0: 4}
dict2_polynomial = transformation_from_list_to_dict(pol2_no_symbols)  # {3: 10, 2: -3, 0: 9}

# Сортирую словари по убыванию, методом get вытаскиваю ключи, если ключи совпадают, то значения ключей складываю
# Если не совпадают, то прибавляю 0
# В конце получаю итоговый словарь, в котором ключи будут из первых двух словарей, а значения ключей будут сложены
result_dict = {}
max_value = max(max(dict1_polynomial), max(dict2_polynomial))
for i in range(max_value, -1, -1):
    sum1 = dict1_polynomial.get(i)
    sum2 = dict2_polynomial.get(i)
    if sum1 != None or sum2 != None:
        result_dict[i] = (sum1 if sum1 != None else 0) + (
            sum2 if sum2 != None else 0)  # {4: 9, 3: 14, 2: -2, 1: 7, 0: 13}

#Собираю из результирующего словаря многочлен
final_dict = ''
for i in result_dict.items():
    if final_dict == '':
        if i[1] < 0:
            final_dict += " - " + str(abs(i[1])) + "x^" + str(abs(i[0]))
        elif i[1] > 0:
            final_dict += str(abs(i[1])) + "x^" + str(abs(i[0]))
    else:
        if i[1] < 0:
            final_dict += " - " + str(abs(i[1])) + "x^" + str(abs(i[0]))
        elif i[1] > 0:
            final_dict += " + " + str(abs(i[1])) + "x^" + str(abs(i[0]))
final_dict = final_dict.replace('x^1 ', 'x ').replace('x^0', '').replace(' 1x^', ' x')

print(final_dict) # 9x^4 + 14x^3 - 2x^2 + 7x + 13 = 0

with open(file_sum, 'w') as data:
    data.writelines(final_dict)
