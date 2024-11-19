import json
import matplotlib.pyplot as plt

FILE_PATH = 'students.json'

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

subjects = ["математика", "фізика", "хімія", "біологія", "історія"]
average_scores = {subject: 0 for subject in subjects}

for student in data["students"]:
    for subject, score in student["scores"].items():
        average_scores[subject] += score

num_students = len(data["students"])
average_scores = {subject: score / num_students for subject, score in average_scores.items()}

labels = list(average_scores.keys())
sizes = list(average_scores.values())
colors = plt.cm.Paired(range(len(labels)))

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("Середні бали по предметах")
plt.axis('equal')
plt.show()
