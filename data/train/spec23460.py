import numpy as np 

def function(x):

	h4 = 2
	g6 = 1
	paths = []
	try:
		if g6 >= 6:
			g6 = 1-h4
			x = 5+1
			paths.append(1)
		else:
			h4 = h4*7
			h4 = h4-0
			paths.append(2)
		if h4 < 7:
			x = 1/x
			paths.append(3)
		else:
			g6 = g6+x
			x = 8+g6
			h4 = h4*h4
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))