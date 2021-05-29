import numpy as np 

def function(x):

	g6 = 3
	x7 = x
	paths = []
	try:
		if x7 < 5:
			x7 = 2*x7
			paths.append(1)
		else:
			x7 = 5+x7
			x7 = x7+2
			paths.append(2)
		if x7 <= 7:
			g6 = 9*g6
			paths.append(3)
		else:
			g6 = g6/7
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