"""Practice working with dictionaries."""

__author__ = "730740372"

def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Swaps the keys and values in a dictionary."""
    new_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in new_dict:
            raise KeyError()
        new_dict[input_dict[key]] = key
    return new_dict

def favorite_color(input_colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    color_count: dict[str, int] = {}
    for key in input_colors:
        if input_colors[key] in color_count:
            color_count[input_colors[key]] += 1
        else:
            color_count[input_colors[key]] = 1
    most_frequent_color: str = ""
    favorite_color_count: int = 0
    for color in color_count:
        if color_count[color] > favorite_color_count:
            most_frequent_color = color
            favorite_color_count = color_count[color]
    return most_frequent_color

def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times an item appears in a list."""
    count_dict: dict[str, int] = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def alphabetizer(alphabet: list[str]) -> dict[str, list[str]]:
    """Keys of dictionary become first letter of items in list, values are lists of items that start with that letter."""
    alphabet_dict: dict[str, list[str]] = {}
    for item in alphabet:
        first_letter: str = item[0].lower()
        if first_letter.isalpha():
            if first_letter in alphabet_dict:
                alphabet_dict[first_letter].append(item)
            else:
                alphabet_dict[first_letter] = [item]
    return alphabet_dict

def update_attendance(attendance: dict[str, list[str]], day_of_week: str, student: str) -> None:
    """Updates the attendance for a student on a given day of the week."""
    if day_of_week in attendance:
        attendance[day_of_week].append(student)
    else:
        attendance[day_of_week] = [student]