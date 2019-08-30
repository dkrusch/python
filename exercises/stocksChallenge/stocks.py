stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'GM', 120, '15-jun-2001', 46 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'EK', 200, '1-jul-1998', 56 )
]

def what_purchased():
    for purchase in purchases:
        print(f'I purchased {stockDict[purchase[0]]} stock for ${purchase[-1]}00.')

def purchased_stocks():
    purchases_of_stocks = {}
    shares_and_price = []
    total = 0
    for i in range(0, len(purchases)):
        shares_and_price.append([purchases[i][1], purchases[i][3]])
        if purchases[i][0] in purchases_of_stocks:
            purchases_of_stocks[purchases[i][0]].append(purchases[i])
        else:
            purchases_of_stocks[purchases[i][0]] = [purchases[i]]

    for name, details in purchases_of_stocks.items():
        print(f"----- {name} -----")
        for detail in details:
            print(f"{detail[1]} shares at {detail[3]} dollars each on {detail[2]}")
        print(f"")

    for things in shares_and_price:
        total += things[0] * things[1]

    print(f"Total value of stock in portfolio: ${total}")

purchased_stocks()