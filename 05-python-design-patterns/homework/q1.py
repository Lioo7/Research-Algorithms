from itertools import combinations
import doctest

class bounded_subsets:
    """
    An iterator that receives as input a list S of different positive numbers,
    and some positive number C, and produces a series of all subsets of S, whose sum is at most C

    >>> for s in bounded_subsets([1,2,3], 4):   print(s)
    [[], [1, 2, 3], (1, 2), (1, 3)]
    """

    def __init__(self, arr: list, bound: int):
        self.arr = sorted(arr)
        self.bound = bound
        self.ans = [[]]
        self.ans.append([x for x in arr if x <= bound])
        self.original_len = len(self.ans)
        self.len = len(self.ans)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.len > self.original_len:
            raise StopIteration()

        for t in range(2, len(self.arr)):
            for combo in combinations(self.arr, t):
                if sum(combo) <= self.bound:
                    self.ans.append(combo)
                    self.len += 1

        return self.ans


if __name__ == "__main__":
    doctest.testmod()

