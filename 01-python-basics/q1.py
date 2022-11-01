def safe_call(f, **kwargs):
    """
    This function gets as input another function and arguments with names, and calls the given function with the given arguments,
    only if the arguments match their corresponding annotations

    >>> safe_call(add, x=5, y=7.0, z=3)
    15.0
    >>> safe_call(add, x=1, y=2.0, z=3.5)
    6.5
    >>> safe_call(avg, x=1.0, y=2.0)
    1.5
    >>> safe_call(sub, w=10, x=1, y=2.0, z=3)
    4.0
    >>> safe_call(add, x=1, y=2, z=3)
    Traceback (most recent call last):
        ...
    Exception: There is a mismatch between the arg's type and its annotation (<class 'int'> != <class 'float'>)
    >>> safe_call(avg, x=1, y=2.0, z=3)
    Traceback (most recent call last):
    ...
    Exception: There is a mismatch between the arg's type and its annotation (<class 'int'> != <class 'float'>)
    """

    func_annotations = f.__annotations__
    args = {}
    # checks for each argument if its type equals its corresponding annotation
    for key, val in kwargs.items():
        args[key] = val
    for key in func_annotations.keys():
        if type(args[key]) is not func_annotations[key]:
            raise Exception(
                f"There is a mismatch between the arg's type and its annotation ({type(args[key])} != {func_annotations[key]})")
    # calls the given function 
    return f(**kwargs)

def add(x: int, y: float, z):
    return x+y+z

def sub(w, x: int, y: float, z):
    return w-x-y-z

def avg(x: float, y: float):
    return (x+y)/2

def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()


