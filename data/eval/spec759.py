import numpy as np 

def function(x):

	c7 = x
	k4 = 4
	paths = []
	try:
		if x <= 9:
			c7 = x-0
			paths.append(1)
		else:
			x = x-k4
			x = 8+9
			paths.append(2)
		if c7 < 1:
			k4 = k4+2
			x = 3*c7
			paths.append(3)
		else:
			c7 = c7*x
			c7 = c7/8
			c7 = k4/2
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