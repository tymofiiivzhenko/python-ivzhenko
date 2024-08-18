N = int(input("Введіть число N: "))

while N < 1 or N > 9:
    print("Число N повинно бути в діапазоні від 1 до 9.")
    N = int(input("Введіть число N: "))

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)

