with open("C:\\Users\\chamo\\OneDrive\\Рабочий стол\\dogheart.txt", "r", encoding = "utf-8") as file:
    c = file.read()
    tokens = c.split(" ")
    print(tokens)