import numpy as np 

def function(x):

	g6 = 4
	c8 = x
	paths = []
	try:
		if c8 > 7:
			x = g6/2
			paths.append(1)
		else:
			x = x-4
			g6 = g6*g6
			paths.append(2)
		if c8 <= 0:
			g6 = c8-g6
			paths.append(3)
		else:
			c8 = c8/x
			x = x-g6
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))