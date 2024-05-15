import nltk
from nltk.stem.snowball import RussianStemmer
nltk.download('punkt')
stemmer = RussianStemmer()
with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:
    text = file.read()
words = nltk.word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in words]
stemmed_text = ' '.join(stemmed_words)
print(stemmed_text)