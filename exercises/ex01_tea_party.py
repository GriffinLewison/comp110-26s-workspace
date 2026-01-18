"""program calculates number of tea bags and treats needed as well as price of tea party based on number of guests attending"""

__author__: str = "730740372"


def main_planner(guests: int) -> None:
    """entrypoint of my program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("")
    print("Treats: " + str(treats(people=guests)))
    print("")
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """returns a value for tea bags based on number of people coming"""
    return people * 2


def treats(people: int) -> int:
    """computes number of treats based on number of teas guests are expected to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculate the total cost of both tea bags and treats"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
