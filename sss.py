with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:
    text = file.read()
n = ''.join([char for char in text if char.isalpha() or char.isspace()])
print(n)