def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def set_operations():
    x = set(range(8, 23))

    y = {num for num in x if is_prime(num)}

    print("Множина x (цілі числа від 8 до 22):", x)
    print("Множина y (прості числа):", y)

set_operations()
