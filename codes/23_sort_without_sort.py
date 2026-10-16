"""Program 23: Sort a list without using sort() or sorted()."""


def bubble_sort(numbers):
    """Return a new list in ascending order (Bubble Sort).

    The original list is not changed.
    """
    result = list(numbers)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print("Sorted:", bubble_sort(data))
