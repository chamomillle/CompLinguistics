#with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:

from collections import Counter

with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:
    text = file.read()

words = text.lower().split()

words = [word.strip('.,!?()[]{}"\'') for word in words]

word_counter = Counter(words)

total_words = sum(word_counter.values())

print("Общее количество слов в тексте:", total_words)