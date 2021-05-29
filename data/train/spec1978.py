import numpy as np 

def function(x):

	x7 = 3
	g6 = 1
	paths = []
	try:
		if g6 <= 3:
			x7 = 6-4
			g6 = 7-g6
			g6 = x7*1
			paths.append(1)
		else:
			g6 = 6+g6
			x = x+x
			paths.append(2)
		if x7 < 6:
			x7 = x7+9
			x = 9*x
			x7 = 8/x
			paths.append(3)
		else:
			x = g6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))