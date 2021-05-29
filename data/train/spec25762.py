import numpy as np 

def function(x):

	g6 = x
	d9 = 4
	x = 0
	paths = []
	try:
		if x < 4:
			x = 5-9
			paths.append(1)
		else:
			g6 = g6*g6
			d9 = d9+3
			g6 = g6-g6
			paths.append(2)
		if g6 <= 7:
			x = g6*x
			g6 = g6+2
			paths.append(3)
		else:
			x = 0*x
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