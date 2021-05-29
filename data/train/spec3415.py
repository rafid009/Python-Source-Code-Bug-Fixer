import numpy as np 

def function(x):

	q4 = x
	c0 = 3
	paths = []
	try:
		if q4 < 9:
			c0 = c0*q4
			paths.append(1)
		else:
			c0 = 3/x
			paths.append(2)
		if q4 <= 6:
			q4 = 1+q4
			x = q4*x
			x = q4/x
			paths.append(3)
		else:
			q4 = c0-q4
			x = 2/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))