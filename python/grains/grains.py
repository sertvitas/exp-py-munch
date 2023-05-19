"""
Calculate grains of wheat on a chess board, given power of 2 at each square
"""

def square(number):
    """
    Grains of wheat on a given square
    :param number:
    :return:
    """
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    grains = 2 ** (number - 1)
    return grains



def total():
    """
    Total grains on the board at a given square
    :param number:
    :return:
    """
    grains = 0
    for n in range(64):
        grains = grains + square(n + 1)
    return grains
