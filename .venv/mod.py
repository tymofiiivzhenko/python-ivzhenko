def mean(x,y):
    evens = [i for i in range(x, y + 1) if i % 2 == 0]

    if len(evens) > 0:
        mean_of_evens = sum(evens) / len(evens)
    else:
        mean_of_evens = 0
    return mean_of_evens

