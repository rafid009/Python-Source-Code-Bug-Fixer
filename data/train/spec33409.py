import numpy as np 

def function(x):

	c1 = 5
	h6 = 1
	paths = []
	try:
		if x >= 1:
			x = 7/x
			paths.append(1)
		else:
			h6 = h6+h6
			c1 = c1-6
			x = 1/h6
			paths.append(2)
		if c1 >= 7:
			h6 = h6-h6
			x = 6-x
			paths.append(3)
		else:
			c1 = c1/1
			h6 = h6-6
			h6 = 9+2
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))