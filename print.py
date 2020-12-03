import sqlite3
from xlsxwriter.workbook import Workbook


workbook = Workbook('Список студентов.xlsx')    # Открытие и запись в файл
worksheet = workbook.add_worksheet()

conn = sqlite3.connect('students.db')   # Подключение к БД
c = conn.cursor()
c.execute("SELECT * FROM students")

print('Выберите направление работы:')
vib = int(input('''1 - Научное студенческое общество;
2 - Социальная поддержка;
3 - Спорт;
4 - Культура и творчество;
5 - Штаб трудовых дел. \n'''))  # Выбор вида работ

if vib == 1:
    mysel = c.execute("SELECT * FROM students WHERE direction_of_work='Научное студенческое общество'")

elif vib == 2:
    mysel = c.execute("SELECT * FROM students WHERE direction_of_work='Социальная поддержка'")

elif vib == 3:
    mysel = c.execute("SELECT * FROM students WHERE direction_of_work='Спорт'")

elif vib == 4:
    mysel = c.execute("SELECT * FROM students WHERE direction_of_work='Культура и творчество'")

elif vib == 5:
    mysel = c.execute("SELECT * FROM students WHERE direction_of_work='Штаб трудовых дел'")

for i, row in enumerate(mysel): # Список выведенных студентов (показывает, что скрипт работает)
    print(row)
    worksheet.write(i, 0, row[0])
    worksheet.write(i, 1, row[1])
    worksheet.write(i, 2, row[2])
    worksheet.write(i, 3, row[3])
    worksheet.write(i, 4, row[4])
    worksheet.write(i, 5, row[5])
    worksheet.write(i, 6, row[6])
    worksheet.write(i, 7, row[7])
workbook.close()
