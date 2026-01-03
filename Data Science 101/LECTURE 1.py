inventory = {

    "Television": 2000.66,
    "Keyboard": 3500.67,
    "Mouse": 4532.23,
    "Monitor": 7002.53,
    "Air Conditioner": 2451.76
}

current_stock = {

    "Television": 50,
    "Keyboard": 34,
    "Mouse": 453,
    "Monitor": 54,
    "Air Conditioner": 21
}

for product, price in inventory.items():
    print(f"The price of {product} is ${price}")

print("\t")

for stock, count in current_stock.items():
    print(f"The current stock of {stock} is {count}")

