
s = input('Введите строку: ')
s_list = list(s)
num = int(input('Введите номер символа: '))
left = s_list[num - 2]
right = s_list[num]

print('Символ слева: ', left)
print('Символ справа: ', right)

if left == s_list[num - 1] and right == s_list[num - 1]:
    print('Есть 2 таких символа')
elif left == s_list[num - 1] or right == s_list[num - 1]:
    print('Есть 1 таких символа')
else:
    print('Таких символов нет')

