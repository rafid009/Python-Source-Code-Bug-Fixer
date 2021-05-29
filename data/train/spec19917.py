import numpy as np 

def function(x):

	a8 = 2
	c9 = 1
	paths = []
	try:
		if c9 < 9:
			a8 = x*2
			c9 = a8/c9
			paths.append(1)
		else:
			a8 = a8-a8
			a8 = a8+3
			paths.append(2)
		if a8 > 4:
			x = x+3
			a8 = a8+a8
			x = x*7
			paths.append(3)
		else:
			x = 5/x
			x = x+6
			c9 = c9*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))