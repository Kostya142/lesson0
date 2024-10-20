from statistics import mean
#Вариант без возможности ввода с клавиатуры новых имён учеников
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik','Aaron' })
print(students)
Aaron=mean(grades[0])
Bilbo=mean(grades[1])
Johnny=mean(grades[2])
Khendrik=mean(grades[3])
Steve=mean(grades[4])
sr_bal=[Aaron, Bilbo, Johnny, Khendrik, Steve]
print(sr_bal)
Final=dict(zip(students, sr_bal))
print(Final)






