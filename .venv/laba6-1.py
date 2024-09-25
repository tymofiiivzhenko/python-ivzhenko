def update_list():

    A = list(map(int, input('Введіть елементи списку: ').split()))
    print("Початковий список:", A)

    even_index_elements = [A[i] for i in range(1, len(A)) if i % 2 == 0]

    A.extend(even_index_elements)

    print("Оновлений список:", A)

    return A

update_list()
