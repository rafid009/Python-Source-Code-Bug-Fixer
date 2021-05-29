import numpy as np 

def function(x):

	a6 = 1
	g6 = 8
	paths = []
	try:
		if g6 < 9:
			a6 = a6*5
			paths.append(1)
		else:
			a6 = a6/a6
			a6 = g6*2
			paths.append(2)
		if x > 1:
			g6 = g6/3
			paths.append(3)
		else:
			a6 = a6-3
			a6 = a6/5
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