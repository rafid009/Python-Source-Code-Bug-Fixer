import numpy as np 

def function(x):

	c0 = 1
	a7 = x
	paths = []
	try:
		if x >= 0:
			x = x-5
			c0 = 3/c0
			a7 = 6+a7
			paths.append(1)
		else:
			x = 6/6
			c0 = 8/c0
			c0 = c0/c0
			paths.append(2)
		if a7 >= 9:
			a7 = a7*x
			x = x/5
			paths.append(3)
		else:
			c0 = 9*c0
			c0 = c0+0
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		c0 = a7**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))