def  test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()   #Ничего не выводится
# inner_function() ---'вызывает ошибку' "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"


def  test_function(): # в явном виде возвращаем указатель на внутреннюю функцию из внешней функции.
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function
test_function()()



