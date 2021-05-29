import numpy as np 

def function(x):

	c4 = x
	q8 = x
	paths = []
	try:
		if c4 >= 5:
			q8 = q8/c4
			c4 = x*c4
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x < 0:
			q8 = c4/2
			paths.append(3)
		else:
			x = 3-x
			c4 = 7+q8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))