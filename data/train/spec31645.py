import numpy as np 

def function(x):

	g6 = 6
	x7 = 6
	x = x
	paths = []
	try:
		if x7 < 2:
			x7 = x7+8
			paths.append(1)
		else:
			x7 = x7-x
			g6 = g6/x7
			paths.append(2)
		if g6 < 6:
			x = x*8
			x = x*6
			paths.append(3)
		else:
			x = x-5
			x7 = x7+x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		g6 = x7**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))