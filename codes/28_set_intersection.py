"""Program 28: Intersection of two sets."""


def set_intersection(first, second):
    """Return a set with only the elements present in both sets."""
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    return result


if __name__ == "__main__":
    a = set(input("Enter first set elements: ").split())
    b = set(input("Enter second set elements: ").split())
    print("Intersection:", set_intersection(a, b))
