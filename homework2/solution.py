# ДЗ Функии

# В `Corp_Summary.csv` лежит выгрузка по сотрудникам: ФИО, департамент, команда, должность, оценка, оклад. Колонки разделены `;`.
#
# Напишите программу, которая читает файл и по выбранному в аргументах варианту готовит отчёт. На экран выводите так, как вам удобно читать.
#
# Варианты отчётов такие. Основная функция должна принимать на вход int - номер варианта. остальные параметры - по желанию:
#
# 1. Иерархия: для каждого департамента показать, какие команды в него входят.
# 2. Сводка по департаментам: название, сколько человек, минимальная и максимальная зарплата, средняя по каждому департаменту.
# 3. То же самое, что в "2", но записанное в csv-файл. Имя выходного файла можно захардкодить(например, константой в начале файла) или передавать опциональным параметром в эту же функцию.
#
# Чтение файла и каждый отчёт вынесите в отдельные функции.


import csv

def read_data():
    with open("Corp_Summary.csv", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))

def hierarchy(rows):
    dct = {}
    for row in rows:
        dept = row['Департамент']
        team = row['Отдел']
        if dept not in dct:
            dct[dept]=[]
        if team not in dct[dept]:
            dct[dept].append(team)
    for dept, teams in dct.items():
        print(f'{dept}:')
        for team in teams:
            print(team)

def departments(rows):
    dct = {}
    for row in rows:
        dept = row['Департамент']
        salary = int(row['Оклад'])
        if dept not in dct:
            dct[dept] = []
        dct[dept].append(salary)
    result = []
    for dept, salaries in dct.items():
        result.append({
            'Департамент': dept,
            'Количество человек': len(salaries),
            'Минимальная зарплата': min(salaries),
            'Максимальная зарплата': max(salaries),
            'Средняя зарплата': round(sum(salaries)/len(salaries),2)
        })
    return result

def report_summary(rows):
    for item in departments(rows):
        print(f"{item['Департамент']}:")
        print(f"Количество человек: {item['Количество человек']}")
        print(f"Минимальная зарплата: {item['Минимальная зарплата']}")
        print(f"Максимальная зарплата: {item['Максимальная зарплата']}")
        print(f"Средняя зарплата: {item['Средняя зарплата']}")

def save_summary(rows, output_file="dept_summary.csv"):
    summary = departments(rows)
    with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(summary)

def main(variant, output_file="dept_summary.csv"):
    rows = read_data()
    if variant == 1:
        hierarchy(rows)
    elif variant == 2:
        report_summary(rows)
    elif variant == 3:
        save_summary(rows, output_file)
    else:
        print('Недопустимый формат ввода')
        

main(1)











