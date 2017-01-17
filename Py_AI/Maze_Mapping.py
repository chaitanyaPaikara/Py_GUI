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
		if index is 4:
			self.delta_list = [ 0, 1, 2, 3]
		else:
			for i in range(index):
				temp = (self.delta_list).pop(0)
				(self.delta_list).append(temp)

		
init = [8, 4]
goal = [0, 3] 
delta = [[ 0,-1,'<'], # go left
         [ 1, 0,'v'], # go down
         [ 0, 1,'>'], # go right
         [-1, 0,'^']] # go up
grid = [[2 for row in range(len(world[0]))] for col in range(len(world))]
grid[init[0]][init[1]] = 0
delta_list = [ 0, 1, 2, 3]
def Mapping(delta):
	last_heading = delta[3]
	flag = True
	me = dynamics(init,last_heading,delta,delta_list)
	for z in range(20):
		heading_flag = True
		for i,j in enumerate(me.delta_list):
			if i is not 1:
				new = [me.pos[0] + delta[j][0], me.pos[1] + delta[j][1]]
				if new[0] >= 0 and new[1] >= 0 and new[0] < len(world) and new[1] < len(world[0]):
					if grid[new[0]][new[1]] is 2:
						grid[new[0]][new[1]] = 1 if world[new[0]][new[1]] else 0
					if heading_flag and world[new[0]][new[1]] is 0:
						me.heading = delta[j]
						if last_heading is not me.heading:
							me.Loop_shift(j+1) 
						print new, me.pos, me.heading, me.delta_list, z
						heading_flag = False
						last_heading = me.heading
		if heading_flag :
			me.U_turn()
			me.Loop_shift((me.delta).index(me.heading)+1)
			print me.heading, me.delta_list 
			#raise SystemExit
		me.moveForward(1)
		if me.pos is goal :
			print "Found Goal"
			flag = False
	return
Mapping(delta)
for z in grid:
	print z





