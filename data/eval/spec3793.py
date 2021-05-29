import numpy as np 

def function(x):

	e3 = 0
	g6 = x
	paths = []
	try:
		if g6 < 7:
			x = 3+x
			paths.append(1)
		else:
			e3 = g6+e3
			x = 0/2
			e3 = e3/7
			paths.append(2)
		if x <= 6:
			g6 = 8/9
			g6 = g6*6
			paths.append(3)
		else:
			g6 = 4/g6
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