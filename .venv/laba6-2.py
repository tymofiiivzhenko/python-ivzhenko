def find_duplicates():

    A = list(map(int, input('Enter a list of numbers: ').split()))

    print("Original list:", A)

    duplicates = [x for x in set(A) if A.count(x) > 1]

    if duplicates:
        print("List of duplicates:", duplicates)
    else:
        print("No duplicates found.")

    return duplicates

find_duplicates()
