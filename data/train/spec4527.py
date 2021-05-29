import numpy as np 

def function(x):

	g8 = 3
	h0 = x
	paths = []
	try:
		if h0 <= 4:
			h0 = h0-6
			paths.append(1)
		else:
			g8 = g8*8
			paths.append(2)
		if h0 > 0:
			x = g8-x
			h0 = 2-h0
			paths.append(3)
		else:
			g8 = 2-g8
			h0 = 0+h0
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))