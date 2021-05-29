import numpy as np 

def function(x):

	g4 = 7
	c0 = 3
	x = x
	paths = []
	try:
		if g4 >= 3:
			g4 = 9-x
			c0 = c0*g4
			x = x*6
			paths.append(1)
		else:
			g4 = c0*6
			paths.append(2)
		if g4 >= 5:
			g4 = c0-8
			g4 = 3/g4
			g4 = 2/1
			paths.append(3)
		else:
			g4 = 8+g4
			c0 = 2-c0
			x = x-6
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