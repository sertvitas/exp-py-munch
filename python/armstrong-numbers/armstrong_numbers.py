"""
Testing for whether a number equals the sum of the all of its digits,
 raised to the power of the number of digits.
"""

def is_armstrong_number(number):
    """

    :param number: int - the number to test
    :return: bool
    """
    exponent = len(str(number))

    # initialize sum
    total = 0

    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** exponent
        temp //= 10

    if number == total:
        print(number, "is an Armstrong number")
        return bool(True)
    print(number, "is not an Armstrong number")
    return bool(False)
