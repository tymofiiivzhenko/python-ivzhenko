amoeba = 1

print("Годин", " ", "Амеб")

for i in range(2, 49, 2):
    amoeba *= 3
    if i in [12, 24, 36, 48]:
        print(i, "    ", amoeba)
