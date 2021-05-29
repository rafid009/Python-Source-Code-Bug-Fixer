import numpy as np 

def function(x):

	g0 = x
	h4 = x
	x = 1
	paths = []
	try:
		if h4 <= 3:
			x = x-3
			g0 = h4+4
			h4 = h4*9
			paths.append(1)
		else:
			h4 = h4-0
			h4 = 7*h4
			paths.append(2)
		if g0 > 8:
			g0 = g0/x
			paths.append(3)
		else:
			g0 = h4*g0
			h4 = 9*h4
			h4 = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))