# Proszę policzyć sumę cen pieces_sold * price_per_item w każdym z kwartałów.
# Brakująca wartość w kolumnie pieces_sold oznacza jeden produkt.

from  datetime import date, datetime

FILE = 'MOCK_DATA.csv'

def liczenie_reve(price, pieces_sold):
    # """
    # >>> import sys; sys.tracebacklimit = 0
    # >>> assert liczenie_reve("1","2") == 2.00
    # >>> assert liczenie_reve("3","") == 3
    # """
    if pieces_sold == "":
        pieces_sold = 1
    else:
        pieces_sold = int(pieces_sold)
    price = float(price)
    revenue = round(pieces_sold * price, 2)
    return revenue

def podzial_lat(data):
    data = datetime.fromisoformat(data)
    lista_2020 = []
    lista_2021 = []
    if data.year == 2020:
        lista_2020.append(data)
    else:
        lista_2021.append(data)
    return lista_2021, lista_2020
    
def podzial_kwartalow(data):
    data = datetime.fromisoformat(data)
    lista_Q1 = []
    lista_Q2 = []
    lista_Q3 = []
    lista_Q4 = []
    
    if data.month in [1,2,3]:
        lista_Q1.append(data)
    elif data.month in [4,5,6]:
        lista_Q2.append(data)
    elif data.month in [7,8,9]:
        lista_Q3.append(data)
    else:
        lista_Q4.append(data)
        
    return lista_Q1, lista_Q2, lista_Q3, lista_Q4
             
        
with open(FILE) as file:
    file.readline()

    years = {"2020 Q1": 0, "2020 Q2": 0, "2020 Q3": 0, "2020 Q4": 0, "2021 Q1": 0, "2021 Q2": 0, "2021 Q3": 0, "2021 Q4": 0}

    for x in file:
        if '"' in x:
            continue
        *reszta,pieces_sold,price_per_item,order_date,shop_id  = x.strip().split(",")
        if pieces_sold == "":
            pieces_sold = 1
        else:
            pieces_sold = int(pieces_sold)

        order_date = datetime.fromisoformat(order_date)
        
    
