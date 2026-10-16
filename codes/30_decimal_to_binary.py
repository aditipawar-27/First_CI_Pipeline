"""Program 30: Convert a decimal number to binary (no bin())."""


def decimal_to_binary(number):
    """Return the binary digits of a non-negative integer as a string.

    0 returns "0"; a negative number raises ValueError.
    """
    if number < 0:
        raise ValueError("Negative numbers are not supported")
    if number == 0:
        return "0"
    digits = ""
    while number > 0:
        digits = str(number % 2) + digits
        number //= 2
    return digits


if __name__ == "__main__":
    n = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(n))
