"""
Collatz Conjecture exercise.
"""
def steps(number):
    """

    :param number: int - starting number for the series
    :return: int - the number of steps it took to get to 1
    """
    # number = int(input('Enter a number: '))
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    sequence = [number]
    while number != 1:
        if(number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        sequence.append(number)
    print(sequence)
    tries = len(sequence)-1
    print(tries)
    return tries
