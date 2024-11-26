import string
import nltk
from nltk import word_tokenize, WordNetLemmatizer, PorterStemmer
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('wordnet')
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

text = gutenberg.raw('shakespeare-hamlet.txt')

word_count = len(nltk.word_tokenize(text))
print(f"Кількість слів у тексті: {word_count}")

tokens = nltk.word_tokenize(text)
word_freq = Counter(tokens)
top_words = word_freq.most_common(10)
print("10 найбільш вживаних слів у тексті:")
for word, freq in top_words:
    print(f"{word}: {freq}")

plt.bar(*zip(*top_words))
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

stopwords = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stopwords]

filtered_word_freq = Counter(filtered_tokens)
filtered_top_words = filtered_word_freq.most_common(10)
print("10 найбільш вживаних слів після видалення стоп-слів та пунктуації:")
for word, freq in filtered_top_words:
    print(f"{word}: {freq}")

plt.bar(*zip(*filtered_top_words))
plt.title('10 найбільш вживаних слів після видалення стоп-слів та пунктуації')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

text_to_save =  (
    "Hold, hold, my heart; "
    "And you, my sinews, grow not instant old, "
    "But bear me stiffly up.--Remember thee! "
    "Ay, thou poor ghost, while memory holds a seat "
    "In this distracted globe. Remember thee! "
    "Yea, from the table of my memory "
    "I'll wipe away all forms, all pressures past, "
    "And thy commandment all alone shall live "
    "Within the book and volume of my brain, "
    "Unmix'd with baser matter: yes, by heaven, "
    "I have sworn't. "
)

with open("input_text.txt", "w", encoding="utf-8") as file:
    file.write(text_to_save)

with open("input_text.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

tokens = word_tokenize(input_text)

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

processed_text = " ".join(filtered_tokens)
with open("processed_text.txt", "w", encoding="utf-8") as file:
    file.write(processed_text)
