import numpy as np 

def function(x):

	h8 = 8
	g0 = x
	paths = []
	try:
		if g0 < 2:
			x = 4/x
			h8 = h8/h8
			paths.append(1)
		else:
			g0 = g0-g0
			x = 1/x
			g0 = 8*7
			paths.append(2)
		if g0 < 2:
			x = x+x
			h8 = h8-3
			paths.append(3)
		else:
			h8 = h8+5
			g0 = 4+h8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))