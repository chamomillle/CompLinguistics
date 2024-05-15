import nltk
nltk.download('punkt')

with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:
    a = file.read()
    tokens = nltk.word_tokenize(a)
    print(tokens)