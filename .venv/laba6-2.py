def find_duplicates():

    A = list(map(int, input('Введіть елементи списку: ').split()))
    print("Початковий список:", A)

    duplicates = [x for x in set(A) if A.count(x) > 1]

    if duplicates:
        print("Список дуплікатів:", duplicates)
    else:
        print("Не знайдено дуплікатів.")

    return duplicates

find_duplicates()
