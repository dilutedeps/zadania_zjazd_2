# Proszę policzyć liczbę sprzedanych produktów w każdym ze sklepów i zwrócić ją jako listę krotek (
# nazwa_sklepu, liczba_produktow) posortowaną malejąco wg liczby produktów.
# Wiersze z pustą nazwą sklepu należy pominąć.
# Brakująca wartość w kolumnie pieces_sold oznacza jeden produkt.

FILE = 'MOCK_DATA.csv'


with open(FILE) as file:
    file.readline()
    lista_sklepow = []

    for x in file:
        if '"' in x:
            continue
        order_id, product_name, pieces_sold, *reszta, shop_id = x.strip().split(",")
        if pieces_sold == "":
            pieces_sold = 1
        else:
            pieces_sold = int(pieces_sold)
        if shop_id != "":
            lista_sklepow.append((shop_id, pieces_sold))


    sklepy = {"shop_1":0, "shop_2":0, "shop_3":0, "shop_4":0}

    for shop_id,pieces in lista_sklepow:
        sklepy[shop_id] += pieces

    print(sorted(sklepy.items(), key=lambda x: x[1], reverse=True))
