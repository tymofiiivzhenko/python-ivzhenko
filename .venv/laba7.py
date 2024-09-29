students = {
    "Kravchuk": [8, 9, 10, 6, 7, 9, 5, 6, 7, 8],
    "Kuchma": [6, 5, 7, 8, 6, 5, 9, 6, 7, 8],
    "Yushchenko": [10, 9, 8, 7, 10, 10, 9, 8, 7, 10],
    "Yanukovych": [5, 4, 6, 7, 6, 5, 4, 7, 6, 5],
    "Poroshenko": [9, 8, 7, 6, 9, 8, 7, 8, 9, 10]
}

def display_students(students_dict):
    for student, grades in students_dict.items():
        print(f"Учень: {student}, Оцінки: {grades}")

def add_student(students_dict, name, grades):
    students_dict[name] = grades
    print(f"Запис для {name} додано.")

def remove_student(students_dict, name):
    try:
        del students_dict[name]
        print(f"Запис для {name} видалено.")
    except KeyError:
        print(f"Запис з ім'ям {name} не знайдено.")

def display_sorted_students(students_dict):
    for student in sorted(students_dict.keys()):
        print(f"Учень: {student}, Оцінки: {students_dict[student]}")

def find_max_sum_student(students_dict):
    max_student = max(students_dict, key=lambda student: sum(students_dict[student]))
    return max_student, sum(students_dict[max_student])

def find_min_sum_student(students_dict):
    min_student = min(students_dict, key=lambda student: sum(students_dict[student]))
    return min_student, sum(students_dict[min_student])

def main():
    while True:
        print("\nМеню:")
        print("1. Вивести всіх учнів та їх оцінки")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Вивести учнів у відсортованому порядку за прізвищами")
        print("5. Знайти учня з найбільшою сумою оцінок")
        print("6. Знайти учня з найменшою сумою оцінок")
        print("7. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            display_students(students)
        elif choice == "2":
            name = input("Введіть прізвище учня: ")
            grades = list(map(int, input("Введіть оцінки через пробіл: ").split()))
            add_student(students, name, grades)
        elif choice == "3":
            name = input("Введіть прізвище учня для видалення: ")
            remove_student(students, name)
        elif choice == "4":
            display_sorted_students(students)
        elif choice == "5":
            max_student, max_sum = find_max_sum_student(students)
            print(f"Учень з найбільшою сумою оцінок: {max_student}, Сума: {max_sum}")
        elif choice == "6":
            min_student, min_sum = find_min_sum_student(students)
            print(f"Учень з найменшою сумою оцінок: {min_student}, Сума: {min_sum}")
        elif choice == "7":
            print("Вихід.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()
