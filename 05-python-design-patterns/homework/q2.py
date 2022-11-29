from typing import Callable, Any

def find_min_max(algorithm: Callable, numbers: Any):
    """
    This program handles a duplicate of code, running four different versions of the same algorithm.
    the algorithm is min_max which gets as an input a list in size>=2 and returns the min and max values.
    Additionally, there are four versions for min_max_sum that returns the sum of the min and max values.

    >>> find_min_max(algorithm=min_max_v1, numbers=[7, 5, 0, 3, 9, 1])
    (0, 9)
    >>> find_min_max(algorithm=min_max_v1, numbers={'a': 7, 'b': 5, 'c': 0, 'd': 3, 'e': 9, 'f': 1})
    (0, 9)
    >>> find_min_max(algorithm=min_max_v2, numbers=[7, 5, 0, 3, 9, 1])
    (0, 9)
    >>> find_min_max(algorithm=min_max_v2, numbers={'a': 7, 'b': 5, 'c': 0, 'd': 3, 'e': 9, 'f': 1})
    (0, 9)

    >>> find_min_max(algorithm=min_max_v3, numbers=[7, 5, 0, 3, 9, 1])
    (0, 9)
    >>> find_min_max(algorithm=min_max_v3, numbers={'a': 7, 'b': 5, 'c': 0, 'd': 3, 'e': 9, 'f': 1})
    (0, 9)

    >>> find_min_max(algorithm=min_max_v4, numbers=[7, 5, 0, 3, 9, 1])
    (0, 9)
    >>> find_min_max(algorithm=min_max_v4, numbers={'a': 7, 'b': 5, 'c': 0, 'd': 3, 'e': 9, 'f': 1})
    (0, 9)

    >>> find_min_max(algorithm=min_max_sum_v1, numbers=[7, 5, 0, 3, 9, 1])
    9
    >>> find_min_max(algorithm=min_max_sum_v2, numbers=[7, 5, 0, 3, 9, 1])
    9
    >>> find_min_max(algorithm=min_max_sum_v3, numbers=[7, 5, 0, 3, 9, 1])
    9
    >>> find_min_max(algorithm=min_max_sum_v4, numbers=[7, 5, 0, 3, 9, 1])
    9
    """
    if isinstance(numbers, dict):  # numbers is a dict
        numbers = list(numbers.values())
    return algorithm(numbers)

def min_max_v1(lst):
    min = max = None
    for num in lst:
        if min is None or num < min:
            min = num
        if max is None or num > max:
            max = num
    return min, max

def min_max_v2(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[0], sorted_lst[-1]

def min_max_v3(lst):
    return min(lst), max(lst)

def min_max_v4(lst):
    min = max = 0
    if lst[0] < lst[1]:
        min = lst[0]
        max = lst[1]
    else:
        max = lst[0]
        min = lst[1]
    for i in range(2, len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
    return min, max

def min_max_sum_v1(lst):
    return sum(min_max_v1(lst))

def min_max_sum_v2(lst):
    return sum(min_max_v2(lst))

def min_max_sum_v3(lst):
    return sum(min_max_v4(lst))

def min_max_sum_v4(lst):
    return sum(min_max_v4(lst))


if __name__ == "__main__":
    import doctest
    # thanks to Erel for the report inspiration
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
