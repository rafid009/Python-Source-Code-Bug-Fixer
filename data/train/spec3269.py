import numpy as np 

def function(x):

	h4 = 9
	q0 = 2
	paths = []
	try:
		if h4 <= 0:
			q0 = q0*9
			q0 = q0-6
			paths.append(1)
		else:
			h4 = 7*h4
			q0 = 6/q0
			paths.append(2)
		if h4 >= 3:
			q0 = x-q0
			q0 = q0/2
			paths.append(3)
		else:
			q0 = 3*5
			x = x-q0
			x = x/4
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))