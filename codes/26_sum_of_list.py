"""Program 26: Sum of the elements in a list (no sum())."""


def sum_of_list(numbers):
    """Return the sum of all elements. An empty list gives 0."""
    total = 0
    for value in numbers:
        total += value
    return total


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print("Sum:", sum_of_list(data))
