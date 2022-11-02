import json

def convert_to_str_then_sort(ds):
    """This function gets a data structure, converts it to string, sorts it and then converts it back to its original structure"""
    match str(type(ds)):
        case "<class 'list'>":
            ds = ' '.join(sorted(str(x) for x in ds))
            ds = list(ds.split(" "))
            return ds
        case "<class 'tuple'>":
            ds = ' '.join(sorted(str(x) for x in ds))
            ds = tuple(ds.split(" "))
            return ds
        case "<class 'dict'>":
            ds = dict(sorted(ds.items()))
            ds = json.dumps(ds)
            ds = json.loads(ds)
            return ds
        case "<class 'set'>":
            ds = ' '.join(sorted(str(x) for x in ds))
            ds = set(ds.split(" "))
            return ds
        case _:
            return ds

def iterate(ds):
    """This function iterates over all the elements in the given data structure"""
    match str(type(ds)):
        case "<class 'list'>":
            for element in ds:
                element = convert_to_str_then_sort(element)
            return ds
        case "<class 'tuple'>":
            for element in ds:
                element = convert_to_str_then_sort(element)
            return ds
        case "<class 'dict'>":
            for key, value in ds.items():
                ds[key] = convert_to_str_then_sort(value)
            return ds
        case "<class 'set'>":
            for element in ds:
                element = convert_to_str_then_sort(element)
            return ds
        case _:
            return ds

def print_sorted(x):
    """
    This function gets as an input a deep data structure, sorting it (in all its levels) and printing it

    >>> print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
    {'a': 5, 'b': ['1', '2', '3', '4'], 'c': 6}
    >>> print_sorted({"a": 5, "c": 6, "b": [1, 3, "dog", 2, "cat", 4]})
    {'a': 5, 'b': ['1', '2', '3', '4', 'cat', 'dog'], 'c': 6}
    >>> print_sorted([5,4,2,0,1])
    ['0', '1', '2', '4', '5']
    """
    updated_ds = convert_to_str_then_sort(x)
    ans = iterate(updated_ds)
    print(ans)


def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
