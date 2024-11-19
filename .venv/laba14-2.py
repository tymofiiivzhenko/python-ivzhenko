import numpy as np
import matplotlib.pyplot as plt
import csv

file_path = 'education.csv'

data = {}
years = []

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    years = [int(col.split()[0]) for col in header[5:]]

    for row in reader:
        country = row[0]
        values = np.array([float(x) if x else np.nan for x in row[5:]])
        data[country] = values

country1 = 'Ukraine'
country2 = 'United Kingdom'

data_country1 = data[country1]
data_country2 = data[country2]

plt.figure(figsize=(10, 5))
plt.plot(years, data_country1, marker='o', label=country1)
plt.plot(years, data_country2, marker='o', label=country2)
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.title('Динаміка показника для двох країн')
plt.legend()
plt.grid(True)
plt.show()

selected_country = input("Введіть назву країни для побудови стовпчастої діаграми: ")
data_selected_country = data.get(selected_country)

if data_selected_country is not None:
    plt.figure(figsize=(8, 5))
    plt.bar(years, data_selected_country)
    plt.xlabel('Рік')
    plt.ylabel('Значення показника')
    plt.title(f'Показник для країни {selected_country}')
    plt.show()
else:
    print(f"Дані для країни {selected_country} відсутні.")
