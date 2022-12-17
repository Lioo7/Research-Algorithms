import numpy
from itertools import combinations
import copy

"""
The two piles difference
https://www.codingame.com/ide/puzzle/the-two-piles-difference

Goal:
You have a list of natural numbers of size N and you must distribute the values in two lists A and B of size N/2, so that the squared sum of the A elements is the nearest possible to the product of the B elements.

Example:
Consider the list 7 11 1 9 10 3 5 13 9 12.
The optimized distribution is:
List A: 5 9 9 12 13
List B: 1 3 7 10 11
which leads to the difference abs( (5+9+9+12+13)^2 - (1*3*7*10*11) ) = 6
Your program should therefore output 6, which is the minimum difference that can be achieved.

Input:
Line 1: The list size N
Line 2: N space separated natural numbers
Output:
Line 1: The minimum difference between the squared sum of elements in list A and the product of elements in list B.

Constraints:
1 <= N <= 40
0 < value of an element < 21
N is always even, so size(A) = size(B).
There are at most 12 different natural numbers.

Example:
Input:
10
7 11 1 9 10 3 5 13 9 12
Output:
6
"""

# This list will contains the input
numbers = []

n = int(input())
for i in input().split():
    value = int(i)
    numbers.append(value)

# The function gets two lists and calculates the abs difference between the sum of the A elements and the product of the B elements
def calculate_abs_diff(sub_list, comp_sub_list):
    squareOfSumA = (sum(sub_list) ** 2)
    productOfB = numpy.prod(comp_sub_list)
    return abs(squareOfSumA - productOfB)

# The function gets as an input two lists, and returns another list that contains all the elements in the original list that not in the sub list
def complement_sublist(original_list, sub_list):
    copy_sub_list = copy.deepcopy(sub_list)
    comp_sub_list = [
        i for i in original_list if not i in copy_sub_list or copy_sub_list.remove(i)]
    return comp_sub_list

# The function gets as an input a list and a number k and returns a list that contains all the sublists in len k of the original list
def find_sublists(lst, k):
    subsets = []
    for subset in combinations(lst, k):
        subsets.append(list(subset))
    return subsets

# The function get a list of positive integers and returns the minimum difference between 
# the squared sum of elements in list A and the product of elements in list B.
def find_min_diff(lst):
    k = int(len(lst)/2)
    sublists = find_sublists(lst, k)
    outcomes = []

    for sublist in sublists:
        comp_sub_list = complement_sublist(lst, list(sublist))
        # print(sublist, comp_sub_list)
        outcome = calculate_abs_diff(sublist, comp_sub_list)
        outcomes.append(outcome)
        # print(outcome)
        if outcome == 0:
            return outcome

    min_diff = min(outcomes)

    return min_diff


ans = find_min_diff(numbers)
print(ans)
