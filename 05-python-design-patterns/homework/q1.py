from itertools import combinations

class bounded_subsets:
    def __init__(self, arr: list, bound: int):
        self.arr = sorted(arr)
        self.bound = bound
        self.ans = [x for x in arr if x <= bound]
        self.original_len = len(self.ans)
        self.len = len(self.ans)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.len > self.original_len:
            raise StopIteration()

        for t in range(2, len(arr)):
            for combo in combinations(arr, t):
                if sum(combo) <= self.bound:
                    self.ans.append(combo)
                    self.len += 1

        return self.ans


def func(arr, bound):
    ans = [x for x in arr if x <= bound]
    for t in range(2, len(arr)):
        for combo in combinations(arr, t): 
            if sum(combo) <= bound:
                ans.append(combo)
    print(ans)
    return ans

if __name__ == "__main__":
    arr = [1,2,3]
    for s in bounded_subsets([1,2,3], 4):
        print(s)

