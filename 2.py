import re

with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:
    text = file.read()
    tokens = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",text)
    print(tokens)