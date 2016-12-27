    # ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
unit_cost = 1
check = [[0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0]]

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,unit_cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path = []
    cost = 0
    init.append(0)
    path.append(init)
    check[path[0][0]][path[0][1]] = 1
    while path:
        for j in delta:
            new = [path[0][0] + j[0],path[0][1] + j[1],path[0][2]]
            if new[0] >= 0 and new[1] >= 0 and new[0] < 5 and new[1] < 6:
                if check[new[0]][new[1]] is 0 and grid[new[0]][new[1]] is 0:
                    if new[0] == goal[0] and new[1] == goal[1]:
                        new[2]+=unit_cost
                        return new
                    else:
                        new[2]+=unit_cost
                        path.append(new)
                        check[new[0]][new[1]] = 1
        del path[0]          

print search(grid,init,goal,unit_cost)