import numpy as np 

def function(x):

	k5 = 4
	g7 = x
	paths = []
	try:
		if g7 < 0:
			g7 = 3-g7
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if g7 <= 5:
			k5 = k5+0
			g7 = x-g7
			paths.append(3)
		else:
			g7 = 3*6
			k5 = k5-g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))