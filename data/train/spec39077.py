import numpy as np 

def function(x):

	c7 = x
	h1 = x
	paths = []
	try:
		if h1 <= 0:
			c7 = c7+c7
			c7 = 4/c7
			x = 6+c7
			paths.append(1)
		else:
			h1 = 4*3
			h1 = 4*h1
			x = 1-x
			paths.append(2)
		if h1 <= 7:
			c7 = c7/7
			c7 = h1/c7
			paths.append(3)
		else:
			c7 = c7+7
			c7 = c7-x
			c7 = 3+c7
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		c7 = h1**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))