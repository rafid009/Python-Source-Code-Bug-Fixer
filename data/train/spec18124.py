import numpy as np 

def function(x):

	g4 = x
	c4 = 1
	paths = []
	try:
		if c4 > 9:
			c4 = 4-g4
			g4 = c4/x
			paths.append(1)
		else:
			c4 = 3/c4
			paths.append(2)
		if c4 <= 9:
			x = x/7
			x = 0-x
			paths.append(3)
		else:
			x = 7+c4
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