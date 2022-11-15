history_calls = {}

def wrap_with_return(func):
    def wrapper(x):
        if x in history_calls:
            print(f"I already told you that the answer is {history_calls[x]}!")
        else:
            ans = func(x)
            history_calls[x] = ans
            return ans
    return wrapper


@wrap_with_return
def f(x: int):
    return x**2


def main():
    # doctest.testmod()
    print(f(2))
    f(2)
    print(f(10))
    f(2)
    f(10)

if __name__ == "__main__":
    main()
