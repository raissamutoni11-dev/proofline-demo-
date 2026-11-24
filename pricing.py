def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")
    return round(price * quantity, 2)


if __name__ == "__main__":
    try:
        price = float(input("Unit price: "))
        quantity = int(input("Quantity: "))
        total = calculate_total(price, quantity)
        print(f"Total: {total:.2f}")
    except ValueError as error:
        print(f"Invalid input: {error}")
