import numpy as np 

def function(x):

	h0 = 8
	g7 = 5
	paths = []
	try:
		if g7 < 4:
			x = x-2
			x = x+x
			paths.append(1)
		else:
			h0 = 9-h0
			h0 = h0+g7
			x = h0/7
			paths.append(2)
		if g7 <= 6:
			x = 8/6
			h0 = 0*g7
			g7 = x-8
			paths.append(3)
		else:
			h0 = h0-3
			g7 = g7/x
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))