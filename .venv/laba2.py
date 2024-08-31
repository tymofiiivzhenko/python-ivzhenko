import math

def calculate_z(m):
    z = math.sqrt(m) + 10
    return z

def mean_of_evens(x, y):
    if x > y:
        return "Помилка: x не може бути більше за y."

    evens = [i for i in range(x, y + 1) if i % 2 == 0]

    if len(evens) > 0:
        mean_value = sum(evens) / len(evens)
    else:
        mean_value = 0

    return mean_value

m = float(input("Введіть значення m: "))

while m < 1:
    print("Значення m не може бути менше за 1.")
    m = float(input("Введіть ще раз значення m: "))

z_result = calculate_z(m)
print("Значення виразу z =", z_result)

x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))

while x > y:
    print("х не може бути більше за у.")
    y = int(input("Введіть ще раз значення y: "))

mean_result = mean_of_evens(x, y)
print("Середнє арифметичне всіх парних чисел від x до y =", mean_result)
