import numpy as np 

def function(x):

	q0 = x
	n4 = 2
	paths = []
	try:
		if x > 0:
			q0 = q0/3
			n4 = n4+3
			n4 = n4-x
			paths.append(1)
		else:
			q0 = 5/q0
			n4 = n4/2
			x = 0*1
			paths.append(2)
		if x <= 9:
			q0 = 4+q0
			n4 = x*x
			paths.append(3)
		else:
			q0 = x+q0
			q0 = 4/q0
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))