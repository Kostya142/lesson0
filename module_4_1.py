from true_math import divide as dtr
from fake_math import divide as dfa
from math import inf
def divide(first, second):
   if second==0:
      return inf
   else:
      return first / second
def divide(first, second):
    if second==0:
       return '<Ошибка>'
    else:
        return first / second
result_1=dtr(1,2)
result_2=dtr(9,0)
result_3=dfa(3,4)
result_4=dfa(3,0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)
