import numpy as np 

def function(x):

	g7 = x
	c9 = x
	paths = []
	try:
		if x >= 6:
			x = x*x
			x = x/c9
			x = 4/x
			paths.append(1)
		else:
			c9 = x/c9
			g7 = g7+4
			paths.append(2)
		if x > 2:
			c9 = c9-7
			g7 = 5-x
			x = 9/x
			paths.append(3)
		else:
			c9 = c9+3
			x = 5/x
			c9 = 8+c9
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))