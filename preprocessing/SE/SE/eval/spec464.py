import numpy as np 

def function(x):

	g5 = x
	h3 = x
	paths = []
	try:
		if h3 < 6:
			g5 = h3/5
			h3 = 8*x
			paths.append(1)
		else:
			x = x/8
			g5 = g5+6
			paths.append(2)
		if g5 < 8:
			h3 = h3-2
			paths.append(3)
		else:
			h3 = 9*2
			h3 = g5*h3
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))