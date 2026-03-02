"""Program that shows utility functions for lists."""

__author__ = "730740372"

def all(list1: list[int], num: int) -> bool:
    """Returns True if all values in the list are the same as the given number; False otherwise."""
    if len(list1) == 0:
        return False
    
    i: int = 0 
    while i < len(list1):
        if list1[i] != num:
            return False
        i += 1
    return True

def max(input: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_num: int = input[0]
    i: int = 1
    while i < len(input):
        if input[i] > max_num:
            max_num = input[i]
        i += 1
    return max_num

def is_equal(a: list[int], b: list[int]) -> bool:
    """Returns True if both lists are equal in both size and values."""
    if len(a) != len(b):
        return False
    
    i: int = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
        i += 1
    return True

def extend(list1: list[int], list2: list[int]) -> None:
    """Appends all values from list2 to the end of list1."""
    i: int = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1