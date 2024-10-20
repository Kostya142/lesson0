from statistics import mean
# Вариант без возможности ввода с клавиатуры новых имён учеников
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_=sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik','Aaron' })
print(students_)
Aaron_=mean(grades[0])
Bilbo_=mean(grades[1])
Johnny_=mean(grades[2])
Khendrik_=mean(grades[3])
Steve_=mean(grades[4])
sr_bal=[Aaron_, Bilbo_, Johnny_, Khendrik_, Steve_]
print(sr_bal)
Final=dict(zip(students, sr_bal))
print(Final)
