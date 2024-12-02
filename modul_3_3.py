def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])
print_params()
print('-----------------')
# print_params(b)  вызывает ошибку
# print_params(a,c) вызывает ошибку
# print_params(a,b,c) вызывает ошибку
values_list=[3,'stroka', False]
values_dict={'a':2, 'b':'stroka', 'c':False}

print_params(*values_list)
print_params(**values_dict)
values_list_2=['pikabu', {1,2,3}]
print_params(*values_list_2,42)




