from datetime import datetime

def find_weekday():
    """
    it will find the day of the weekday
    the weekdays are represented 0 is monday, 6 is sunday
    """
    today = datetime.now()
    weekday = today.weekday()
    return weekday

def calculates_without_discount(subtotal):
    sales_tax = (subtotal * 6) / 100
    total = subtotal + sales_tax
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")

def calculates_with_discount(subtotal):
    discount = (subtotal * 10) / 100
    sales_tax = ((subtotal - discount) * 6) / 100
    total = subtotal - discount + sales_tax
    print(f"Discount amount: ${discount:.2f}")
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")


subtotal = 0

while True:
    item_price = float(input("Insert the item price: "))
    if item_price == 0:
        break

    amount = int(input("Insert the amount of items: "))
    subtotal += (item_price * amount)
    print("Price has been stored\n")

if find_weekday() == 1 or find_weekday() == 2:
    if subtotal >= 50:
        print()
        print("-=-" * 15)
        calculates_with_discount(subtotal)
        print("-=-" * 15)

    else:
        difference = 50 - subtotal
        print()
        print("-=-" * 15)
        print(f"You needed ${difference:.2f} to get a discount.")
        calculates_without_discount(subtotal)
        print("-=-" * 15)

else:
    print()
    print("-=-" * 15)
    calculates_without_discount(subtotal)
    print("-=-" * 15)
