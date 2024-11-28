calls = 0   
def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    count_calls()
    for i in list_to_search:
        if i.lower() == string:
            result_ = True
            break
        else:
            result_ = False
            continue
    return result_

print(string_info('Klipsa'))
print(string_info('Podkrilok'))
print(is_contains('DranDuLet', ['Tent', 'drandulet', 'Drandulichka', 'Dranduler'])) # Urban ~ urBAN
print(is_contains('Shkvoren', ['bolt', 'stopor', 'ftulka'])) # No matches

print(calls)


