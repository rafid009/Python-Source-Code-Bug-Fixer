import numpy as np 

def function(x):

	g0 = 6
	c8 = 2
	paths = []
	try:
		if c8 >= 5:
			c8 = 7/x
			x = c8*4
			paths.append(1)
		else:
			g0 = g0-7
			g0 = 7/c8
			c8 = 7-x
			paths.append(2)
		if x < 4:
			g0 = 8+1
			g0 = g0/g0
			x = 2/x
			paths.append(3)
		else:
			c8 = 8*c8
			g0 = g0/1
			g0 = g0-c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))