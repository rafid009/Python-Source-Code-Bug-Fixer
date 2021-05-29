import numpy as np 

def function(x):

	b3 = 0
	c5 = 4
	paths = []
	try:
		if c5 >= 8:
			c5 = b3/c5
			paths.append(1)
		else:
			c5 = 7/1
			c5 = 3*9
			paths.append(2)
		if c5 > 6:
			b3 = 5*x
			paths.append(3)
		else:
			x = b3/x
			c5 = c5-x
			c5 = 3-c5
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		c5 = b3**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))