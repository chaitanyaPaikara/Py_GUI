#World to map 
world = [[1,1,1,0,1,1,1,1,1],
		 [1,0,0,0,1,0,0,1,0],
		 [1,0,1,0,1,0,1,1,1],
		 [1,0,1,0,0,0,0,0,1],
		 [1,0,1,1,1,1,0,1,1],
		 [1,0,1,0,0,0,0,0,1],
		 [1,1,1,1,0,1,1,0,1],
		 [1,0,0,0,0,1,0,0,1],
		 [1,1,1,1,0,1,1,1,1]]

delta_list = [ 0, 1, 2, 3]

class dynamics(object):
	def __init__(self,pos,heading,delta,delta_list):
		self.pos = pos
		self.heading = heading
		self.delta = delta
		self.delta_list = delta_list
	def moveForward(self,steps):
		for i in range(steps):
			self.pos = [self.pos[0] + self.heading[0], self.pos[1] + self.heading[1]]
	def print_parameters(self):
		print self.pos, self.heading, self.delta, self.delta_list
	def U_turn(self):
		cursor = (self.delta).index(self.heading)
		cursor += 2
		self.heading = self.delta[cursor % 4]
	def Loop_shift(self,index):
		llist = [ 0, 1, 2, 3]
		if index is 2:
			self.delta_list = llist 
		else:
			if index is 4:
				index = 2
			for i in range(index):
				temp = llist.pop(-1)
				llist.insert( 0, temp)
			self.delta_list = llist	

		
init = [8, 4]
goal = [0, 3] 
delta = [[ 0,-1,'<'], # go left
         [-1, 0,'^'], # go up
         [ 0, 1,'>'], # go right
         [ 1, 0,'v']] # go down
grid = [[9 for row in range(len(world[0]))] for col in range(len(world))]
X = [[0 for row in range(len(world[0]))] for col in range(len(world))]
grid[init[0]][init[1]] = 0
def Mapping(delta):
	last_heading = [-1, 0,'^']
	flag = True
	me = dynamics(init,last_heading,delta,delta_list)
	while flag :
		X[me.pos[0]][me.pos[1]] += 1
		limit = 2
		for j in me.delta_list:
			new = [me.pos[0] + delta[j][0], me.pos[1] + delta[j][1]]
			if new[0] >= 0 and new[1] >= 0 and new[0] < len(world) and new[1] < len(world[0]):
				grid[new[0]][new[1]] = 1 if world[new[0]][new[1]] else 0
				if world[new[0]][new[1]] is 0 and X[new[0]][new[1]] < 2:
					if X[new[0]][new[1]] < limit:
						limit = X[new[0]][new[1]]
						me.heading = delta[j]
						if last_heading is not me.heading:
							me.Loop_shift(j+1) 
						last_heading = me.heading
						#print new, me.pos, me.heading, me.delta_list, j
		last_pos = me.pos
		me.moveForward(1)
		if me.pos[0] is goal[0] and me.pos[1] is goal[1] :
			#print "Found Goal"
			flag = False
	return

print init[0], init[1], goal[0], goal[1]
Mapping(delta)
for row in grid:
	for col in row:
		print col,
	print '\r'
'''
print '************************************************'
for z in X:
	print z
'''




