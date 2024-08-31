def mean_of_evens(x, y):
    if x > y:
        return "Помилка: x не може бути більше за y."
    evens = [i for i in range(x, y + 1) if i % 2 == 0]
    if len(evens) > 0:
        mean_value = sum(evens) / len(evens)
    else:
        mean_value = 0
    return mean_value

