from typing import Any


def four_neighbor_function(node:Any)->list:
    (x,y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def breadth_first_search(start, end, neighbor_function):
    return 

def main():
    breadth_first_search(start=(0,0), end=(2,2), neighbor_function=four_neighbor_function)


if __name__ == "__main__":
    main()
