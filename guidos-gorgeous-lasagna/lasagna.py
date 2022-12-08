"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2



def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(layers: int) -> int:
    """Calculate prep time
    :param layers: int - number of layers in the finished lasagna
    :return: int - prep time in minutes based on the number of layers
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int,elapsed_bake_time: int) -> int:
    """
    :param layers: int - number of layers
    :param elapsed_bake_time: int - minutes in the oven
    :return: elapsed_time_in_minutes: int - length of time so far, based on prep time and current bake time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
