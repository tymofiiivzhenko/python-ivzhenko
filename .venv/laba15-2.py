import pandas as pd
import matplotlib.pyplot as plt

file_path = 'laba15-2.csv'
data_frame = pd.read_csv(file_path)

data_frame['Date'] = pd.to_datetime(data_frame['Date'])

data_frame['Місяць'] = data_frame['Date'].dt.month

monthly_totals = data_frame.groupby('Місяць').sum(numeric_only=True)

print(monthly_totals)

monthly_totals['Кількість велосипедистів'] = monthly_totals.sum(axis=1)

plt.figure(figsize=(10, 6))
monthly_totals['Кількість велосипедистів'].plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Кількість велосипедистів за кожен місяць 2013 року', fontsize=16)
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.xticks(ticks=range(12), labels=range(1, 13), rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()

max_cyclists_month = monthly_totals['Кількість велосипедистів'].idxmax()
max_cyclists_count = monthly_totals['Кількість велосипедистів'].max()

months_dict = {
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}

max_month_name = months_dict[max_cyclists_month]

print("Найбільш популярним місяцем у велосипедистів у 2013 був", max_month_name)
print("Кількість велосипедистів цього місяця:", max_cyclists_count)
