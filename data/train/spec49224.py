import numpy as np 

def function(x):

	g8 = x
	h0 = 8
	paths = []
	try:
		if h0 >= 1:
			h0 = h0-0
			paths.append(1)
		else:
			g8 = x-g8
			h0 = x-0
			paths.append(2)
		if g8 < 6:
			h0 = h0-9
			g8 = g8*0
			paths.append(3)
		else:
			x = x*g8
			h0 = x+0
			g8 = 6-g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		h0 = g8**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))