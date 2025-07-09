# import csv - wczytuje narzędzie do pracy z plikami CSV"
import csv

data = [["imie", "nazwisko", "wiek"],
        ["Jan", "Kowalski", 30],
        ["Anna", "Nowak", 25],
        ["Piotr", "Zielinski", 40]]

# newline="" - mówi Pythonowi: „Nie dodawaj automatycznie dodatkowych znaków nowej linii przy zapisie do pliku”, dwa cudzysłowy na końcu mówią, że nie chcemy żadnych znaków specjalnych przy zapisie do pliku CSV.
# "" - bez dodawania znaków specjalnych
# "\n" - nowa linia (! Ważne \ i / ma znaczenie)
# "\r\n" - nowa linia i powrót do początku linii (typowe dla Windows)

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("data.csv", "r") as file:
    # reader - dzięki temu możemy czytać plik CSV wiersz po wierszu
    # csv.reader(file) - dzięki temy możemy czytać plik CSV
    reader = csv.reader(file)
    # for row in reader - przechodzi przez każdy wiersz w pliku CSV
    for row in reader:
        print(row)