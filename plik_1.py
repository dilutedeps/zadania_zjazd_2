# Proszę wczytać plik i wyświetlić pierwsze 10 nazw produktów posortowane w kolejności alfabetycznej.

FILE = 'MOCK_DATA.csv'

with open(FILE) as file:
    file.readline()
    nazwy = []
    for x in file:
        if '"' in x:
            continue
        indeks, nazwa, *reszta = x.strip().split(",")
        nazwy.append(nazwa)
        nazwy.sort()

print(nazwy[:10])








