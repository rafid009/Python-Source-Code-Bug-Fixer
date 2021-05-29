import numpy as np 

def function(x):

	k4 = 5
	c6 = 0
	x = x
	paths = []
	try:
		if x <= 5:
			k4 = k4-c6
			x = k4+x
			k4 = k4*k4
			paths.append(1)
		else:
			k4 = 9+6
			c6 = c6+k4
			x = 6/x
			paths.append(2)
		if k4 < 8:
			c6 = 3/6
			paths.append(3)
		else:
			k4 = k4*k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))