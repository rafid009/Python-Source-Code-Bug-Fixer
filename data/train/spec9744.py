import numpy as np 

def function(x):

	c1 = x
	g7 = x
	paths = []
	try:
		if x >= 6:
			g7 = c1/c1
			g7 = 7/g7
			paths.append(1)
		else:
			g7 = g7-x
			paths.append(2)
		if x <= 2:
			g7 = 0-5
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		c1 = g7**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))