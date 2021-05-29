import numpy as np 

def function(x):

	g7 = x
	h3 = 5
	paths = []
	try:
		if g7 > 1:
			g7 = g7*x
			paths.append(1)
		else:
			h3 = 7+6
			x = h3+g7
			paths.append(2)
		if h3 < 0:
			h3 = h3+4
			paths.append(3)
		else:
			g7 = 7*g7
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))