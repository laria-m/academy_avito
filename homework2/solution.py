import csv


def read_data():
    with open("Corp_Summary.csv", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))


def hierarchy(rows):
    departments_teams = {}
    for row in rows:
        dept = row["Департамент"]
        team = row["Отдел"]
        if dept not in departments_teams:
            departments_teams[dept] = []
        if team not in departments_teams[dept]:
            departments_teams[dept].append(team)
    for dept, teams in departments_teams.items():
        print(f"{dept}:")
        for team in teams:
            print(team)


def departments(rows):
    departments_salaries = {}
    for row in rows:
        dept = row["Департамент"]
        salary = int(row["Оклад"])
        if dept not in departments_salaries:
            departments_salaries[dept] = []
        departments_salaries[dept].append(salary)
    result = []
    for dept, salaries in departments_salaries.items():
        result.append({
            "Департамент": dept,
            "Количество человек": len(salaries),
            "Минимальная зарплата": min(salaries),
            "Максимальная зарплата": max(salaries),
            "Средняя зарплата": round(sum(salaries) / len(salaries), 2)
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
        print("Недопустимый формат ввода")
        

if __name__ == "__main__":
    variant = int(input("Введите номер отчета:"))
    main(variant)
    




