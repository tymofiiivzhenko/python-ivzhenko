import pandas as pd

students = {
    "Kravchuk": [8, 9, 10, 6, 7, 9, 5, 6, 7, 8],
    "Kuchma": [6, 5, 7, 8, 6, 5, 9, 6, 7, 8],
    "Yushchenko": [10, 9, 8, 7, 10, 10, 9, 8, 7, 10],
    "Yanukovych": [5, 4, 6, 7, 6, 5, 4, 7, 6, 5],
    "Poroshenko": [9, 8, 7, 6, 9, 8, 7, 8, 9, 10],
}

df = pd.DataFrame(students)

df["Zelenskyy"] = [10, 8, 10, 7, 9, 8, 7, 8, 7, 8]

print("DataFrame зі студентами:")
print(df)

df["Середній бал"] = df.mean(axis=1)

def categorize_grade(avg):
    if avg < 7:
        return "Низький"
    elif 7 <= avg < 8:
        return "Середній"
    else:
        return "Високий"

df["Рівень"] = df["Середній бал"].apply(categorize_grade)

print("\nDataFrame після агрегації та групування:")
print(df)

grouped = df.groupby("Рівень").size()

print("\nГрупування за рівнем:")
print(grouped)


