import numpy as np 

def function(x):

	h3 = 1
	c9 = x
	paths = []
	try:
		if h3 >= 1:
			c9 = 4*c9
			h3 = c9-6
			h3 = h3/9
			paths.append(1)
		else:
			c9 = c9*h3
			x = 4*1
			paths.append(2)
		if h3 <= 5:
			x = 5+6
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		c9 = h3**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))