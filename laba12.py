import json

FILE_PATH = 'students.json'
EXTREMES_FILE_PATH = 'extreme_scores.json'

def load_data():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"students": []}

def save_data(data):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_extremes(max_student=None, min_student=None):
    try:
        with open(EXTREMES_FILE_PATH, 'r', encoding='utf-8') as file:
            extremes_data = json.load(file)
    except FileNotFoundError:
        extremes_data = {}

    if max_student:
        extremes_data["max_score_student"] = max_student
    if min_student:
        extremes_data["min_score_student"] = min_student

    with open(EXTREMES_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(extremes_data, file, ensure_ascii=False, indent=4)
    print("Дані збережено в extreme_scores.json.")

def display_data():
    data = load_data()
    if data["students"]:
        for student in data["students"]:
            print(f"Прізвище: {student['name']}, Оцінки: {student['scores']}")
    else:
        print("Файл порожній або не існує.")

def add_student():
    data = load_data()
    name = input("Введіть прізвище учня: ")
    scores = {}
    for subject in ["математика", "фізика", "хімія", "біологія", "історія"]:
        score = int(input(f"Введіть оцінку з предмету {subject}: "))
        scores[subject] = score
    data["students"].append({"name": name, "scores": scores})
    save_data(data)
    print("Додано нового учня.")

def delete_student():
    data = load_data()
    name = input("Введіть прізвище учня, якого бажаєте видалити: ")
    new_data = [student for student in data["students"] if student['name'] != name]
    if len(new_data) != len(data["students"]):
        data["students"] = new_data
        save_data(data)
        print(f"Учня з прізвищем {name} видалено.")
    else:
        print(f"Учня з прізвищем {name} не знайдено.")

def search_student():
    data = load_data()
    name = input("Введіть прізвище для пошуку: ")
    found = False
    for student in data["students"]:
        if student['name'] == name:
            print(f"Прізвище: {student['name']}, Оцінки: {student['scores']}")
            found = True
    if not found:
        print("Учня з таким прізвищем не знайдено.")

def find_max_student(data):
    student_sums = [
        {"name": student["name"], "total": sum(student["scores"].values())}
        for student in data["students"]
    ]
    max_student = max(student_sums, key=lambda x: x["total"])

    print(f"Учень з найбільшою сумою оцінок: {max_student['name']} ({max_student['total']})")
    save_extremes(max_student=max_student)
    return max_student

def find_min_student(data):
    student_sums = [
        {"name": student["name"], "total": sum(student["scores"].values())}
        for student in data["students"]
    ]
    min_student = min(student_sums, key=lambda x: x["total"])

    print(f"Учень з найменшою сумою оцінок: {min_student['name']} ({min_student['total']})")
    save_extremes(min_student=min_student)
    return min_student

def main():
    while True:
        print("\nОберіть дію:")
        print("1 - Вивести вміст JSON файлу")
        print("2 - Додати нового учня")
        print("3 - Видалити учня")
        print("4 - Пошук учня за прізвищем")
        print("5 - Знайти учня з найбільшою сумою оцінок")
        print("6 - Знайти учня з найменшою сумою оцінок")
        print("7 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            display_data()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            data = load_data()
            find_max_student(data)
        elif choice == '6':
            data = load_data()
            find_min_student(data)
        elif choice == '7':
            print("Вихід із програми.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
