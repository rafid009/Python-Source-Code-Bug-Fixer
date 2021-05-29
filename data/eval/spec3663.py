import numpy as np 

def function(x):

	q0 = 6
	h6 = x
	paths = []
	try:
		if q0 < 3:
			h6 = 0-h6
			q0 = x*q0
			paths.append(1)
		else:
			x = 1-h6
			paths.append(2)
		if q0 >= 2:
			x = 0*x
			q0 = 1-8
			q0 = 3-q0
			paths.append(3)
		else:
			h6 = 3*h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		q0 = h6**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))