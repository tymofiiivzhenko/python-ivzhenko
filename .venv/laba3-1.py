word = str(input("Введіть слово: "))

while len(word) < 3:
    word = str(input("Слово занадто коротке. Введіть слово ще раз: "))

new_word = word[1] + word[-2]

print("Після зрізу другого та передостаннього символів: ", new_word)
