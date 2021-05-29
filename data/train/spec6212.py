import numpy as np 

def function(x):

	h6 = 1
	c9 = 4
	paths = []
	try:
		if c9 >= 7:
			c9 = c9/8
			paths.append(1)
		else:
			x = 7-6
			paths.append(2)
		if h6 >= 9:
			c9 = 4-x
			c9 = 8*6
			c9 = 9/c9
			paths.append(3)
		else:
			h6 = h6-9
			h6 = h6*7
			c9 = c9-4
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))