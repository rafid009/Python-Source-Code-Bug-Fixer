import numpy as np 

def function(x):

	q0 = 5
	k4 = x
	paths = []
	try:
		if q0 < 7:
			x = 5*x
			paths.append(1)
		else:
			k4 = k4-k4
			x = 3+6
			paths.append(2)
		if q0 < 6:
			x = 1-x
			paths.append(3)
		else:
			x = 7-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))