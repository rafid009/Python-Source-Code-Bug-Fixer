import numpy as np 

def function(x):

	c1 = 5
	f9 = 6
	paths = []
	try:
		if c1 < 2:
			c1 = c1/1
			x = 4/x
			paths.append(1)
		else:
			x = x*7
			c1 = c1-6
			x = f9-0
			paths.append(2)
		if c1 < 4:
			c1 = c1/c1
			x = x-8
			f9 = 8/5
			paths.append(3)
		else:
			f9 = 6/f9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))