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


with open(FILE) as file:
    file.readline()

    sum_weekends = 0
    for x in file:
        if '"' in x:
            continue
        *reszta,pieces_sold,price_per_item,order_date,shop_id  = x.strip().split(",")
        if pieces_sold == "":
            pieces_sold = 1
        else:
            pieces_sold = int(pieces_sold)

        order_date = datetime.fromisoformat(order_date)

        if order_date.isoweekday() in [6,7]:
            sum_weekends +=  liczenie_reve(price_per_item,pieces_sold)

    print(sum_weekends)