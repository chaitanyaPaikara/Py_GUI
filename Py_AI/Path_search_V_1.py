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
thing = []
class stuff(object):
    def __init__(self,last_pos,possibility,last_action):
        self.possibility = possibility
        self.last_pos = last_pos
        self.last_action = last_action

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
    track = 1
    index = 0
    possibility = []
    while Flag:
        for j in delta:
            new = [pos[0] + j[0],pos[1] + j[1]]
            if new[0] >= 0 and new[1] >= 0 and new[0] < len(grid) and new[1] < len(grid[0]):
                if cost[new[0]][new[1]] is track:
                    index+=1
                    possibility.append(j)    	
    	if index is 0:
            del thing[len(thing)-1].possibility[0]
            pos = thing[len(thing)-1].last_pos
            #print pos
            #print thing[len(thing)-1].possibility
            track = cost[pos[0]][pos[1]] + 2
            #print track
            pos = [pos[0] + thing[len(thing)-1].possibility[0][0], pos[1] + thing[len(thing)-1].possibility[0][1]]
        else:
            if index > 1:
                thing.append(stuff(pos,possibility,possibility[0][2]))
                last_pos = pos                        
            action[pos[0]][pos[1]] = possibility[0][2]
            pos = [pos[0] + possibility[0][0], pos[1] + possibility[0][1]]
            possibility = []
            track += 1
        if pos[0] == goal[0] and pos[1] == goal[1]:
            Flag = False
            action[pos[0]][pos[1]] = 'g'
        index = 0
print search(grid,init,goal,unit_cost)
print
for z in cost:
    print z

traversal(unit_cost,cost,init,delta)
for z in action:
    print z
#for z in expand:
#    print z
