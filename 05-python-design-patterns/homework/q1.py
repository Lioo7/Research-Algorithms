from itertools import combinations
import doctest

class bounded_subsets:
    """
    An iterator that receives as input a list S of different positive numbers,
    and some positive number C, and produces a series of all subsets of S, whose sum is at most C

    >>> for s in bounded_subsets([1,2,3], 4):   print(s)
    [], [1], [2], [3], [1, 2], [1, 3]

    >>> for s in bounded_subsets(range(50,150), 103):   print(s)
    [], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99], [100], [101], [102], [103], [50, 51], [50, 52], [50, 53]

    >>> for s in zip(range(5), bounded_subsets(range(100), 10)): print(s) 
    (0, []), (1, [0]), (2, [1]), (3, [2]), (4, [3])

    >>> for s in bounded_subsets([2,3,4,5], 1):   print(s)
    [[]]
    """

    def __init__(self, arr: list, bound: int):
        self.arr = sorted(arr)
        self.bound = bound
        self.ans = [[]]
        if self.arr[0] <= bound: [self.ans.append([x]) for x in arr if x <= bound]
        self.status = True

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.status:
            raise StopIteration()

        for t in range(2, min(len(self.arr), self.bound)):
            for combo in combinations(self.arr, t):
                if sum(combo) <= self.bound:
                    self.ans.append(list(combo))
                else:
                    break

        self.status = False

        return self.ans


if __name__ == "__main__":
    doctest.testmod()

    # for s in bounded_subsets(range(100), 10):
    #     print(s)

    # for s in zip(range(5), bounded_subsets(range(100), 10)):
    #     print(s)

