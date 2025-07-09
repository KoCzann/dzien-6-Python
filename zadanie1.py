import csv

# stworzam listę z imieniem i wiekiem
dane = [["imie", "wiek"]]

# zbieram dane od użytkownika i wpisuje do listy z imieniem i wiekiem
for i in range(3):
    data = input("Wprowadź Imie i wiek oddzielone przecinkami: ")
    dane.append(data.split(","))

#  tworze, uzupełniam i odczytuje plik csv z danymi
with open("ludzie.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(dane)

with open("ludzie.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  

# stworzyłam liste, która zliczy ile osób ma więcej niż 20 lat
data = [0]

# stprawdzam ile osób ma więcej niż 20 lat i dodaje do listy
data = 0

for osoba in dane[1:]:
    wiek = int(osoba[1].strip())
    if wiek > 20:
        data += 1

# wynik końcowy
print(f"Powyżej jest lista osób które wpisałeś i ich wiek, na tej liście tyle osób, które mają więcej niż 20 lat: {data}")
