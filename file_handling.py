# Wpisywanie czegoś do pliku - zamienia wszystko co było w pliku na to co wpiszemy
with open("example.txt", "w") as file:
    file.write("1. Hello, World!\n")
    file.write("This is a new line.\n")

# Dopisywanie do pliku - dopisuje to co wpiszemy na końcu pliku
with open("example.txt", "a") as file:
    file.write("2. Kolejna czesc tego co chce napisac\n")
    file.write("A tutaj jeszcze kolejna\n")

# otwieranie i czytanie pliku
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
