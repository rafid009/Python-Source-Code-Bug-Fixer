import numpy as np 

def function(x):

	g6 = x
	e4 = x
	paths = []
	try:
		if g6 < 2:
			x = x-7
			x = x-4
			g6 = 5-g6
			paths.append(1)
		else:
			g6 = 7/g6
			g6 = e4/g6
			paths.append(2)
		if e4 < 7:
			e4 = e4-g6
			paths.append(3)
		else:
			e4 = 5+e4
			e4 = g6/4
			g6 = g6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))