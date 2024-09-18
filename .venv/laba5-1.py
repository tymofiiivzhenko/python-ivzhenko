n = int(input("n = "))
print(f"Введіть {n} елементів масиву:")
arr = [float(input()) for _ in range(n)]
print("Одновимірний масив:", arr)

max_negative = None

for num in arr:
    if num < 0:
        if max_negative is None or num < max_negative:
            max_negative = num

if max_negative is not None:
    print(f"Максимальний від'ємний елемент: {max_negative}")
else:
    print("У масиві немає від'ємних елементів.")

