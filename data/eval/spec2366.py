import numpy as np 

def function(x):

	f5 = 5
	c5 = 1
	paths = []
	try:
		if x >= 3:
			x = 6/5
			paths.append(1)
		else:
			c5 = f5-0
			c5 = c5*1
			f5 = 7-f5
			paths.append(2)
		if c5 > 2:
			c5 = c5-0
			x = x+8
			paths.append(3)
		else:
			c5 = 1-x
			c5 = c5*x
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))