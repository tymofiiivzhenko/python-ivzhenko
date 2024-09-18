n = 7
a = [[j - i if j >= i else -(i - j) for j in range(n)] for i in range(n)]
for r in a:
    print(' '.join(f"{num:3}" for num in r))
