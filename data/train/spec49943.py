import numpy as np 

def function(x):

	g9 = 6
	h0 = x
	paths = []
	try:
		if h0 >= 4:
			g9 = h0-h0
			g9 = h0*7
			x = 0+7
			paths.append(1)
		else:
			g9 = g9*4
			paths.append(2)
		if x <= 6:
			g9 = g9-g9
			g9 = 6/9
			paths.append(3)
		else:
			g9 = g9-x
			g9 = 6-g9
			g9 = 1*h0
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