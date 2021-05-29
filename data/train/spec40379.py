import numpy as np 

def function(x):

	c8 = 6
	g5 = 3
	paths = []
	try:
		if c8 <= 7:
			x = x+c8
			paths.append(1)
		else:
			x = x*3
			x = g5+x
			paths.append(2)
		if x <= 7:
			g5 = g5+0
			paths.append(3)
		else:
			c8 = x-9
			c8 = 0/c8
			c8 = c8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))