import numpy as np 

def function(x):

	c4 = 5
	h8 = 5
	paths = []
	try:
		if x > 4:
			x = 5-h8
			paths.append(1)
		else:
			h8 = 5+x
			paths.append(2)
		if x >= 5:
			c4 = 5-1
			paths.append(3)
		else:
			h8 = h8-3
			c4 = c4-c4
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		c4 = h8**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))