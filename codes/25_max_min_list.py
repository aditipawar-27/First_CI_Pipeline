"""Program 25: Find the maximum and minimum in a list (no max()/min())."""


def find_max_min(numbers):
    """Return a tuple (maximum, minimum). Raise ValueError for an empty list."""
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    maximum = minimum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    return (maximum, minimum)


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    high, low = find_max_min(data)
    print("Maximum:", high)
    print("Minimum:", low)
