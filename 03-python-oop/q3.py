""""
>>> arr1 = List([1, 2, 3])
>>> print(arr1[0])
1

>>> arr2 = List([[1, 2, 3],[4,5,6]])
>>> print(arr2[1][1])
5

>>> arr3 = List([[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]], ])
>>> print(arr3[0, 1, 3]) 
66

>>> arr4 = List([[[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]], ], [[100, 200, 300],[[10, 10, 20],[1, 2, 3]]]])
>>> print(arr4[1, 1, 0, 2])
20

counsulted with a friend about the approach 
"""

import doctest

class List(list):
    """A structure named list, which is Python's list (list), but can access details in a multidimensional array syntax"""
    def __init__(self, arr):
        super().__init__(arr)
    
    def __getitem__(self, *indices):
        try:
            sub_arr = super().__getitem__(indices[0])

        except:
            sub_arr = super().__getitem__(indices[0][0])
            for index in indices[0][1:]:
                sub_arr = sub_arr[index]

        return sub_arr


def main():
    doctest.testmod()

if __name__ == "__main__":
    main()
