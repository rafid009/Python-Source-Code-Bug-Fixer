import numpy as np 

def function(x):

	h9 = 5
	q1 = 7
	paths = []
	try:
		if x >= 4:
			q1 = q1-h9
			x = q1*q1
			paths.append(1)
		else:
			q1 = 7-q1
			paths.append(2)
		if h9 < 8:
			h9 = h9*x
			q1 = 4+q1
			paths.append(3)
		else:
			x = 1/3
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))