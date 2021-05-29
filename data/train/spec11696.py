import numpy as np 

def function(x):

	g7 = x
	u4 = x
	paths = []
	try:
		if x >= 6:
			g7 = 7*g7
			u4 = 1*u4
			paths.append(1)
		else:
			g7 = g7+u4
			g7 = g7/4
			u4 = g7-x
			paths.append(2)
		if x >= 9:
			x = x-g7
			x = x/g7
			paths.append(3)
		else:
			g7 = g7*6
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