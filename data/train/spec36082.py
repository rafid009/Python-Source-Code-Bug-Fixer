import numpy as np 

def function(x):

	g5 = 9
	c4 = 1
	paths = []
	try:
		if c4 < 5:
			x = x-4
			paths.append(1)
		else:
			x = c4*x
			c4 = c4-c4
			paths.append(2)
		if c4 < 5:
			c4 = c4-c4
			g5 = 4+g5
			c4 = c4*9
			paths.append(3)
		else:
			x = 0+x
			c4 = 4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))