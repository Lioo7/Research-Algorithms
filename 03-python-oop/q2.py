"""
>>> print(pow(2))
4
>>> pow(2)
I already told you that the answer is 4!
>>> print(pow(10))
100
>>> pow(2)
I already told you that the answer is 4!
>>> pow(10)
I already told you that the answer is 100!

>>> print(duplicate("Hello"))
HelloHello
>>> duplicate("Hello")
I already told you that the answer is HelloHello!
>>> print(duplicate("World"))
WorldWorld
>>> duplicate("Hello")
I already told you that the answer is HelloHello!
>>> duplicate("World")
I already told you that the answer is WorldWorld!

>>> print(round_up(2.3))
3.0
>>> round_up(2.3)
I already told you that the answer is 3.0!
>>> print(round_up(10.5))
11.0
>>> round_up(2.3)
I already told you that the answer is 3.0!
>>> round_up(10.5)
I already told you that the answer is 11.0!
"""

import numpy as np
import doctest

history_calls = {} # this dict will save all the inputs of the user and their results 

def last_input(func):
    """
    this function gets another function as an input and wrapped it,
    in order to warn if the user inserts the same input multiple times
    """
    def wrapper(x):
        if x in history_calls:
            print(f"I already told you that the answer is {history_calls[x]}!")
        else:
            ans = func(x)
            history_calls[x] = ans
            return ans
    return wrapper


@last_input
def pow(x: int):
    return x**2

@last_input
def duplicate(s: str):
    return s*2

@last_input
def round_up(x: float):
     return np.ceil(x)


def main():
    doctest.testmod()

if __name__ == "__main__":
    main()
