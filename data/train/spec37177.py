import numpy as np 

def function(x):

	c3 = 2
	g4 = 3
	x = x
	paths = []
	try:
		if g4 > 6:
			g4 = 3+g4
			paths.append(1)
		else:
			g4 = g4-c3
			paths.append(2)
		if g4 > 0:
			c3 = 3-c3
			paths.append(3)
		else:
			g4 = 5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))