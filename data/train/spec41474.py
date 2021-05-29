import numpy as np 

def function(x):

	g4 = 1
	c3 = 6
	paths = []
	try:
		if g4 < 8:
			x = c3-x
			paths.append(1)
		else:
			g4 = c3/c3
			paths.append(2)
		if g4 >= 9:
			c3 = 8+c3
			paths.append(3)
		else:
			g4 = g4+9
			c3 = 5*9
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