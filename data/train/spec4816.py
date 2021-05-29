import numpy as np 

def function(x):

	g9 = 6
	h0 = 0
	paths = []
	try:
		if h0 > 3:
			x = 0/x
			h0 = h0*7
			h0 = h0*h0
			paths.append(1)
		else:
			h0 = 0-x
			h0 = 1/h0
			paths.append(2)
		if x >= 8:
			h0 = h0/2
			x = x+g9
			x = x*x
			paths.append(3)
		else:
			g9 = h0+3
			g9 = g9-x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))