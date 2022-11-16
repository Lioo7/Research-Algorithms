"""
*Remaining Card*
link: https://www.codingame.com/ide/puzzle/remaining-card
Goal
You have N cards in a stack. Each card has a different number written on it.

The top card is written 1. The second card is written 2. The third card is written 3...
The sequence continues to the last card (the bottom card) which is written N.

Repeat the following operations until the stack of cards is reduced to 1 card:
➀ throw away the top card
② move the current top card to the bottom

You got one last card in hand. What is the number written on it?
Input
Line 1: an integer N
Output
Line 1: the number on the remaining card
Constraints
1 ≤ N ≤ 1,000,000,000

Be aware of the very high upper limit. Design a fast algorithm to solve it.

credit: my little borther helped me solving this question 
"""

import math

n = int(input())

# *Solution 1 - naive algorithm*
# # initilazes a deck of n cards
# deck = [i for i in range(1, n+1)]

# while(len(deck) > 1):
#     deck.pop(0) # throws away the top card
#     deck.append(deck.pop(0)) # moves the current top card to the bottom

# print(deck[0])

# *Solution 2 - efficient algorithm*
# if the log of the number in base 2 is a whole number then print n
log_n_base_2 = math.log(n, 2)
if log_n_base_2.is_integer():
    print(n)

else:
    # round the log of the number in base 2 down
    log_n_base_2 = int(math.log(n, 2))
    # calculates the biggest power in base 2 which less than n
    biggest_power = 2**log_n_base_2
    # the last card in the deck will be the num of jumps of 2 from the biggest poweer till n
    last_card = 2 * (n - biggest_power)
    print(last_card)
