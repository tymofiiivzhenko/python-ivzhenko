def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не відкрився")
        return None
    else:
        print("Файл", file_name, "відкрився")
        return file

file1_name = "TF19_1.txt"
file_1_w = Open(file1_name, "w")

if file_1_w != None:
    file_1_w.write("Слово.\n")
    file_1_w.write("Два  слова.\n")
    file_1_w.write("А три слова.\n")
    print("Інформація була успішно додана до TF19_1.txt!")
    file_1_w.close()
    print("Файл TF19_1.txt був закритий!")

# Виведення вмісту першого файлу
print("Вміст TF19_1.txt:")
file_1_r = Open(file1_name, "r")

if file_1_r != None:
    for line in file_1_r:
        print(line.strip())
    file_1_r.close()
    print("Файл TF19_1.txt був закритий!")

file2_name = "TF19_2.txt"
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r != None and file_2_w != None:
    for line in file_2_r:
        words = line.split()
        filtered_words = [word for word in words if len(word) > 1]
        file_2_w.write(" ".join(filtered_words) + '\n')

    file_2_r.close()
    file_2_w.close()
    print("Файли були закриті!")

print("Новий вміст TF19_2.txt:")
file_3_r = Open(file2_name, "r")

if file_3_r != None:
    for line in file_3_r:
        print(line.strip())
    file_3_r.close()
    print("Файл TF19_2.txt був закритий!")
