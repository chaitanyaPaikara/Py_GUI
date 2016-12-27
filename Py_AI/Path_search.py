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
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
unit_cost = 1
check = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
action = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
action[0][0] = 's' 
action[len(grid)-1][len(grid[0])-1] = 'g' 
delta = [[-1, 0,'^'], # go up
         [ 0,-1,'<'], # go left
         [ 1, 0,'v'], # go down
         [ 0, 1,'>']] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,unit_cost):
    path = []
    init.append(0)
    path.append(init)
    check[path[0][0]][path[0][1]] = 1
    while path:
        print path     
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
                        action[new[0]][new[1]] = j[2]
                        check[new[0]][new[1]] = 1
        del path[0]   
'''
def traversal(action):
    current = init
    while current is not goal:
        for j in delta:
            new = [current[0] + j[0],current[1] + j[1]]
            if new[0] >= 0 and new[1] >= 0 and new[0] < 5 and new[1] < 6:
                if action[new[0]][new[1]] is not ' ':
                    
'''

print search(grid,init,goal,unit_cost)
for z in action:
    print z