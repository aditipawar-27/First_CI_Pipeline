"""Program 27: Rotate a list by k positions."""


def rotate_list(items, k):
    """Rotate the list to the right by k positions and return a new list.

    k may be larger than the list length; a negative k rotates left.
    An empty list returns [].
    """
    if not items:
        return []
    k = k % len(items)
    if k == 0:
        return list(items)
    return items[-k:] + items[:-k]


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    steps = int(input("Enter k: "))
    print("Rotated:", rotate_list(data, steps))
