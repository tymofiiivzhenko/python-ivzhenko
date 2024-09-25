def find_duplicates():

    A = list(map(int, input('Enter a list of numbers: ').split()))

    print("Original list:", A)

    duplicates = [x for x in set(A) if A.count(x) > 1]

    print("List of duplicates:", duplicates)

    return duplicates

find_duplicates()
