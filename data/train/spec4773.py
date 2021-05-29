import numpy as np 

def function(x):

	c3 = 4
	f7 = 8
	paths = []
	try:
		if x >= 5:
			f7 = c3-f7
			f7 = 9*c3
			c3 = c3/c3
			paths.append(1)
		else:
			c3 = x-f7
			paths.append(2)
		if x < 5:
			x = x+x
			c3 = c3/2
			paths.append(3)
		else:
			c3 = 8/x
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))