import numpy as np 

def function(x):

	q0 = 6
	c4 = x
	paths = []
	try:
		if c4 < 8:
			q0 = x*q0
			paths.append(1)
		else:
			x = x/5
			c4 = c4-5
			paths.append(2)
		if c4 > 1:
			q0 = q0/5
			c4 = 1-c4
			q0 = q0-5
			paths.append(3)
		else:
			c4 = c4+x
			q0 = 9+4
			x = q0*x
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