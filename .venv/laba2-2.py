from mod import mean_of_evens
import math

x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))
while x > y:
    print("х не може бути більше за у.")
    y = int(input("Введіть ще раз значення y: "))
print("Середнє арифметичне всіх парних чисел від x до y =", mean_of_evens(x,y))
