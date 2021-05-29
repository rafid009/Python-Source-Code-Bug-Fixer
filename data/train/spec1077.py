import numpy as np 

def function(x):

	u0 = 0
	c8 = 5
	paths = []
	try:
		if x < 5:
			c8 = x-c8
			u0 = c8*x
			paths.append(1)
		else:
			u0 = u0-3
			c8 = 7+4
			paths.append(2)
		if c8 >= 3:
			x = 3/x
			paths.append(3)
		else:
			x = x/c8
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))