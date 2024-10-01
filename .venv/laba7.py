students = {
    "Kravchuk": [8, 9, 10, 6, 7, 9, 5, 6, 7, 8],
    "Kuchma": [6, 5, 7, 8, 6, 5, 9, 6, 7, 8],
    "Yushchenko": [10, 9, 8, 7, 10, 10, 9, 8, 7, 10],
    "Yanukovych": [5, 4, 6, 7, 6, 5, 4, 7, 6, 5],
    "Poroshenko": [9, 8, 7, 6, 9, 8, 7, 8, 9, 10]
}

def Print(students):
    for i in students:
        print("Оцінки", i, " - ", students[i])

def add(students, key, grade):
    students[key] = grade
    print("Добавлено", key, ".")

def Del(students, key):
    try:
        del students[key]
        print("Видалено", key, ".")
    except KeyError:
        print(f"Учень з ім'ям {key} не знайдений.")

def print_sort(students):
    students_sorted = {k: students[k] for k in sorted(students)}
    print("Відсортований словник: ")
    for i in students_sorted:
        print("Оцінки", i, " - ", students_sorted[i])

def find_max_sum_student(students):
    max_student = max(students, key=lambda student: sum(students[student]))
    return max_student, sum(students[max_student])

def find_min_sum_student(students):
    min_student = min(students, key=lambda student: sum(students[student]))
    return min_student, sum(students[min_student])

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
            Print(students)
        elif choice == "2":
            name = input("Введіть прізвище учня: ")
            grades = list(map(int, input("Введіть оцінки через пробіл: ").split()))
            add(students, name, grades)
        elif choice == "3":
            name = input("Введіть прізвище учня для видалення: ")
            Del(students, name)
        elif choice == "4":
            print_sort(students)
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
