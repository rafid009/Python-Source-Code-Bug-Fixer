import numpy as np 

def function(x):

	c1 = 8
	c6 = 7
	paths = []
	try:
		if c1 >= 1:
			x = x+x
			paths.append(1)
		else:
			x = 7-3
			paths.append(2)
		if c1 <= 7:
			c1 = x+5
			c1 = x/c1
			x = x*5
			paths.append(3)
		else:
			x = 3-x
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