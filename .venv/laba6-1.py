def update_list():

    A = list(map(int, input('Enter a list: ').split()))
    print("Initial list:", A)

    even_index_elements = [A[i] for i in range(1, len(A)) if i % 2 == 0]

    A.extend(even_index_elements)

    print("Updated list:", A)

    return A

update_list()
