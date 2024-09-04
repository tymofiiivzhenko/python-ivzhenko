word = input("Введіть слово: ")

new_word = ""

for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        new_word += word[i]

print("Слово після видалення однакових символів:", new_word)
