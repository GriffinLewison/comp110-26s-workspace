def celsius_to_fahrenheit(degrees: int) -> float:
    return (degrees * 9 / 5) + 32


def perimeter(length: float, width: float) -> float:
    """calculate the perimeter of a rectangle"""
    return length * 2 + width * 2


def total_cost(price: int, tax_rate: float) -> float:
    return price + (price * tax_rate)


print(total_cost(price=100, tax_rate=0.07))


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))


def pos_or_neg(num: int) -> str:
    if num > 0:
        return "Positive"
    else:
        return "Negative"
