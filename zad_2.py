#Dla każdego wiersza w pliku, proszę policzyć całkowitą cenę zakupu:
#pieces_sold * price_per_item. Brakująca wartość w kolumnie pieces_sold oznacza jeden produkt.

FILE = 'MOCK_DATA.csv'

def liczenie_reve(price, pieces_sold):
    """
    >>> import sys; sys.tracebacklimit = 0
    >>> assert liczenie_reve("1","2") == 2.00
    >>> assert liczenie_reve("3","") == 3
    """
    if pieces_sold == "":
        pieces_sold = 1
    else:
        pieces_sold = int(pieces_sold)
    price = float(price)
    revenue = round(pieces_sold * price, 2)
    return revenue


with open(FILE) as file:
    file.readline()
    revenues = []
    for x in file:
        if '"' in x:
            continue
        indeks, nazwa, pieces_sold, price, *reszta = x.strip().split(",")
        wynik = liczenie_reve(price, pieces_sold)
        revenues.append(wynik)

print(revenues[:5])
