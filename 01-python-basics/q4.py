"""
Rock Paper Scissors Lizard Spock
https://www.codingame.com/ide/puzzle/rock-paper-scissors-lizard-spock
Goal
An international Rock Paper Scissors Lizard Spock tournament is organized, all players receive a number when they register.

Each player chooses a sign that he will keep throughout the tournament among:
Rock (R)
Paper (P)
sCissors (C)
Lizard (L)
Spock (S)

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
and in case of a tie, the player with the lowest number wins (it's scandalous but it's the rule).

Example
4 R \
      1 P \
1 P /      \
             1 P
8 P \      /     \
      8 P /       \
3 R /              \
                     2 L
7 C \              /
      5 S \       /
5 S /      \     /
             2 L
6 L \      /
      2 L /
2 L /
The winner of the tournament is player 2. Before winning, he faced player 6, then player 5 and finally player 1.
Input
Line 1: an integer N representing the number of participants in the competition
Lines 2 to N+1: an integer NUMPLAYER indicating the player number (players have distinct numbers between 1 and N) followed by a letter 'R', 'P', 'C', 'L' or 'S' indicating the chosen sign SIGNPLAYER
Output
Line 1: the number of the winner
Line 2: the list of its opponents separated by spaces
Constraints
N is a 2^k value (2, 4, 8, 16, ..., 1024)
2 ≤ N ≤ 1024
Example
Input
8
4 R
1 P
8 P
3 R
7 C
5 S
6 L
2 L
Output
2
6 5 1
"""

# This function return the player who lost in the battle
def battle(p1, p1_num, p2, p2_num):
    loser = ""
    if p1 == 'C' and p2 == 'P':
        loser = p2_num
    elif p1 == 'P' and p2 == 'R':
        loser = p2_num
    elif p1 == 'R' and p2 == 'L':
        loser = p2_num
    elif p1 == 'L' and p2 == 'S':
        loser = p2_num
    elif p1 == 'S' and p2 == 'C':
        loser = p2_num
    elif p1 == 'C' and p2 == 'L':
        loser = p2_num
    elif p1 == 'L' and p2 == 'P':
        loser = p2_num
    elif p1 == 'P' and p2 == 'S':
        loser = p2_num
    elif p1 == 'S' and p2 == 'R':
        loser = p2_num
    elif p1 == 'R' and p2 == 'C':
        loser = p2_num
    elif p1 == p2:
        loser = p2_num if p1_num < p2_num else p1_num
    else:
        loser = p1_num
    return loser


participants = {}
players_in_the_game = []
opponents = {}

n = int(input())
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    participants[numplayer] = signplayer
    players_in_the_game.append(numplayer)
    opponents[numplayer] = []

i = 0
while (len(players_in_the_game) > 1):
    # generates the battles by their order
    p1_num = players_in_the_game[i]
    p1_sign = participants[p1_num]
    p2_num = players_in_the_game[i+1]
    p2_sign = participants[p2_num]
    # gets the loser bewtween both of the players
    loser = battle(p1_sign, p1_num, p2_sign, p2_num)
    # finds the winner
    winner = p1_num if p2_num == loser else p2_num
    # remove the the palyer that lost
    players_in_the_game.remove(int(loser))
    # add the player that lost to the opponents dict
    opponents[winner].append(loser)
    i = (i + 1) % len(players_in_the_game)

tournament_winner = players_in_the_game[0]
opponents_str = s = ' '.join(str(x) for x in opponents[tournament_winner])

print(tournament_winner)
print(opponents_str)
