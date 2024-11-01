import csv
import os

file_path = 'laba11-db.csv'

if not os.path.exists(file_path):
    print(f"Помилка: Файл '{file_path}' не знайдено.")
else:
    try:
        max_fdi = {"Country Name": None, "Country Code": None, "2015 [YR2015]": float('-inf')}
        min_fdi = {"Country Name": None, "Country Code": None, "2015 [YR2015]": float('inf')}

        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Вміст початкового файлу:")
            for row in reader:
                print(row)

                try:
                    fdi_value = float(row["2015 [YR2015]"])

                    if fdi_value > max_fdi["2015 [YR2015]"]:
                        max_fdi = {"Country Name": row["Country Name"], "Country Code": row["Country Code"],
                                   "2015 [YR2015]": fdi_value}
                    if fdi_value < min_fdi["2015 [YR2015]"]:
                        min_fdi = {"Country Name": row["Country Name"], "Country Code": row["Country Code"],
                                   "2015 [YR2015]": fdi_value}
                except ValueError:
                    continue

        output_file_path = 'fdi_min_max_2015.csv'

        with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Country Name", "Country Code", "2015 [YR2015]"])
            writer.writeheader()
            writer.writerow(max_fdi)
            writer.writerow(min_fdi)

        if os.path.exists(output_file_path):
            print(f"\nФайл з результатами успішно створено: {output_file_path}")
        else:
            print("Помилка: Не вдалося створити вихідний файл.")

    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
