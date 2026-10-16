"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    """Return True if both strings use the same letters.

    Upper/lower case and spaces are ignored.
    """
    a = "".join(first.split()).lower()
    b = "".join(second.split()).lower()
    if len(a) != len(b):
        return False
    counts = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Anagrams:", is_anagram(s1, s2))
