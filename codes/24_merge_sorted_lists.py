"""Program 24: Merge two sorted lists into one sorted list."""


def merge_sorted_lists(list1, list2):
    """Return one sorted list containing all elements of both lists."""
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


if __name__ == "__main__":
    a = [int(x) for x in input("Enter first sorted list: ").split()]
    b = [int(x) for x in input("Enter second sorted list: ").split()]
    print("Merged:", merge_sorted_lists(a, b))
