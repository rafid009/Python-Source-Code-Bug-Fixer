import numpy as np 

def function(x):

	h0 = x
	g9 = 3
	paths = []
	try:
		if g9 >= 6:
			g9 = g9-6
			x = g9+0
			g9 = h0*7
			paths.append(1)
		else:
			g9 = g9-3
			x = x*1
			g9 = g9-6
			paths.append(2)
		if h0 >= 9:
			h0 = h0-0
			x = h0+h0
			paths.append(3)
		else:
			g9 = g9/2
			g9 = g9-g9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))