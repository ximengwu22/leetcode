"""
Given a n*n grid where each cell has one of three values :
0 represents an empty cell
1 represents there is a cheese in the cell
2 represents there is a rat in the cell.

Now the rat has a special ability that he can clone himself four times and go upward(i-1, j), right(i, j+1), down(i+1, j), left(i, j-1). The rat will only go to the given directions if a cheese is in there in the cell he can go all for directions and eat in 1 second.

Find the minimum time he needs to eat all Cheese available in the grid.
If it is impossible to eat all the cheese then return -1.

Input format :
The first line contains an integer n representing the size of the array,
Then there are n lines which contains n space separated integers representing the array grid.

Output :
Return minimum time required to eat all cheese available.
"""

# flake8: noqa
def minTimeToEatALlCheese(arr: list):
    n, m = len(arr), len(arr[0])
    cheeses = set()
    rats = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cheeses.add((i, j))
            elif arr[i][j] == 2:
                rats.add((i, j))
    # bfs
    days = 0
    while rats:
        if not cheeses: break
        num_of_rats = len(rats)
        for i in range(num_of_rats):
            rati, ratj = rats.pop()
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = rati+di, ratj+dj
                if 0 <= x < n and 0 <= y < m and (x, y) in cheeses:
                    cheeses.remove((x, y))
                    rats.add((x, y))
        days += 1
    return days if not cheeses else -1

assert(minTimeToEatALlCheese([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4)
assert(minTimeToEatALlCheese([[2,1,1],[0,1,1],[1,0,1]]) == -1)