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


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0]]
'''
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
'''
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
unit_cost = 1
cost = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
check = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
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
    time = 0
    init.append(0)
    path.append(init)
    check[path[0][0]][path[0][1]] = 1
    while path:
        print path, "\t"+str(time)    
        for j in delta:
            new = [path[0][0] + j[0],path[0][1] + j[1],path[0][2]]
            if new[0] >= 0 and new[1] >= 0 and new[0] < len(grid) and new[1] < len(grid[0]):
                if check[new[0]][new[1]] is 0 and grid[new[0]][new[1]] is 0:
                    if new[0] == goal[0] and new[1] == goal[1]:
                        new[2]+=unit_cost
                        cost[new[0]][new[1]] = new[2]
                        expand[new[0]][new[1]] = time
                        return new
                    else:
                        new[2]+=unit_cost
                        cost[new[0]][new[1]] = new[2]
                        path.append(new)
                        #action[new[0]][new[1]] = j[2]
                        #action[path[0][0]][path[0][1]] = j[2]
                        check[new[0]][new[1]] = 1
                elif grid[new[0]][new[1]] is 1:
                    expand[new[0]][new[1]] = -1
        del path[0]   
        expand[path[0][0]][path[0][1]] = time
        time+=unit_cost


def traversal(unit_cost,cost,init,delta):
    Flag = True
    pos = init
    track = 0
    index = 0
    possibility = []
    last_pos = []
    while Flag:
        if pos is not last_pos:
            track+=unit_cost
            for j in range(len(delta)):
                new = [pos[0] + delta[j][0],pos[1] + delta[j][1]]
                if new[0] >= 0 and new[1] >= 0 and new[0] < len(grid) and new[1] < len(grid[0]):
                    if cost[new[0]][new[1]] is track:
                        action[pos[0]][pos[1]] = delta[j][2]
                        postion = new
                        index+=1
                        if index > 1:
                            last_pos = pos
                            possibility.append(delta[j])
        else:
            for j in range(len(possibility)):
                if possibility[j][2] is last_action:
                    del possibility[j]
                else:
                    new = [pos[0] + possibility[j][0],pos[1] + possibility[j][1]]
                    if new[0] >= 0 and new[1] >= 0 and new[0] < len(grid) and new[1] < len(grid[0]):
                        if cost[new[0]][new[1]] is track:
                            action[pos[0]][pos[1]] = possibility[j][2]
                            index+=1
                            if index > 1:
                                last_pos = pos
        if index == 0:
            pos = last_pos
        else:
            last_action = action[pos[0]][pos[1]]
            pos = postion
        index = 0
        if pos[0] == goal[0] and pos[1] == goal[1]:
            Flag = False
            action[pos[0]][pos[1]] = 'g'
print search(grid,init,goal,unit_cost)
print
for z in cost:
    print z

traversal(unit_cost,cost,init,delta)
for z in action:
    print z
#for z in expand:
#    print z
