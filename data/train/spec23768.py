import numpy as np 

def function(x):

	g4 = 7
	c0 = 4
	paths = []
	try:
		if g4 > 0:
			x = 7/5
			paths.append(1)
		else:
			x = 8+6
			paths.append(2)
		if g4 > 0:
			c0 = c0*3
			x = x-8
			x = 6+x
			paths.append(3)
		else:
			x = g4-x
			c0 = c0/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))