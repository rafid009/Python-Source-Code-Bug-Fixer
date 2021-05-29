import numpy as np 

def function(x):

	h9 = 5
	c1 = 5
	paths = []
	try:
		if x >= 2:
			h9 = h9+5
			h9 = 9+h9
			c1 = c1-h9
			paths.append(1)
		else:
			c1 = 2/c1
			paths.append(2)
		if c1 > 6:
			x = 8*x
			h9 = 1*h9
			paths.append(3)
		else:
			h9 = h9*c1
			c1 = 6-c1
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		x = h9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))