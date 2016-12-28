import Robot_Class 
import random

def main():
	myrobot = Robot_Class.robot()
	myrobot = myrobot.move(0.1, 5.0)
	Z = myrobot.sense()
	N = 1000
	p = []
	for i in range(N):
	    x = Robot_Class.robot()
	    x.set_noise(0.05, 0.05, 5.0)
	    p.append(x)

	p2 = []
	for i in range(N):
	    p2.append(p[i].move(0.1, 5.0))
	p = p2

	w = []
	for i in range(N):
	    w.append(p[i].measurement_prob(Z))

	p3 = []
	beta = 0
	w_max = max(w)
	index = int(random.random()*N)
	for i in range(N):
	    beta = beta + (2*w_max*random.random())
	    while w[index] < beta:
	        beta = beta - w[index]
	        index = (index + 1)%N
	    p3.append(p[index])
	    
	p = p3
	print p

#################################################################
#          P - Controller
def run(param1,param2):
    myrobot = Robot_Class.robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0 # motion distance is equal to speed (we assume time = 1)
    N = 100
    error = myrobot.y
    prev_error = myrobot.y
    for i in range(N):
    	error = myrobot.y
    	#error_diff = error - prev_error
        steering = -param1*error #- param2*error_diff 
        myrobot = myrobot.move(steering,1)
        print myrobot, i
        #prev_error = error
        
run(0.1,3.0) # call function with parameter tau of 0.1 and print results

