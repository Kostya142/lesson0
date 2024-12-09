def get_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    if str_number[0]=='0':
        return 1
    elif len(str_number) >1 :
        return first * get_digits(int(str_number[1:]))
    else:
        return first
num = input('Введите целое число: ')
print(f'Произведение цифр числа {num} :', get_digits(num))



