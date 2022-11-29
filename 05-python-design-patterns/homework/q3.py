"""
link: https://www.codingame.com/ide/puzzle/super-computer

In the Computer2000 data center, you are responsible for planning the usage of a supercomputer for scientists.
​Therefore you've decided to organize things a bit by planning everybody’s tasks.
The logic is simple: the higher the number of calculations which can be performed, the more people you can satisfy.

Rules
Scientists give you the starting day of their calculation and the number of consecutive days they need to reserve the calculator.

For example:
Calculation	Starting Day	Duration
A	2	5
B	9	7
C	15	6
D	9	3	
Calculation A starts on day 2 and ends on day 6

Calculation B starts on day 9 and ends on day 15

Calculation starts on day 15 and ends on day 20

Calculation D starts on day 9 and ends on day 11

In this example, it’s not possible to carry out all the calculations because the periods for B and C overlap.
3 calculations maximum can be carried out: A, D and C.
"""

def sort_dict(value):
    return value[0] + value[1] - 1

calendar = {}
counter = 1

n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    if j in calendar:
        if d < calendar[j]:
            calendar[j] = d
    else:
        calendar[j] = d

clend_lst = list(calendar.items())
clend_lst.sort(key=sort_dict)

end_curr_exper = clend_lst[0][0] + clend_lst[0][1] - 1
for i, exper in enumerate(clend_lst):
    if i+1 < len(clend_lst): 
        start_next_exper = clend_lst[i+1][0]
        if start_next_exper > end_curr_exper:
            end_curr_exper = clend_lst[i+1][0] + clend_lst[i+1][1] - 1
            counter += 1

print(counter)


