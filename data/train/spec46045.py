import numpy as np 

def function(x):

	h9 = 4
	g1 = 2
	paths = []
	try:
		if h9 <= 6:
			g1 = g1/7
			g1 = g1-6
			paths.append(1)
		else:
			g1 = h9+g1
			x = 6/7
			paths.append(2)
		if x > 8:
			g1 = h9*2
			g1 = 9+3
			g1 = g1*x
			paths.append(3)
		else:
			h9 = 2*4
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))