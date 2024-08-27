from mod import mean
import math

m = float(input("Введіть значення m: "))
z = math.sqrt(m) + 10
print("Значення виразу z =", z)

x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))

while x > y:
    print("х не може бути більше за у.")
    y = int(input("Введіть ще раз значення y: "))

print("Середнє арифметичне всіх парних чисел від x до y =", mean(x,y))

