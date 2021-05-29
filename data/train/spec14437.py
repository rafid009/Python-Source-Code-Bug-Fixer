import numpy as np 

def function(x):

	q4 = 3
	c6 = x
	x = x
	paths = []
	try:
		if c6 > 0:
			x = 0+x
			paths.append(1)
		else:
			q4 = q4-q4
			paths.append(2)
		if c6 >= 0:
			x = 5+6
			q4 = q4-x
			paths.append(3)
		else:
			c6 = 7/c6
			x = q4-x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		c6 = q4**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))