import numpy as np 

def function(x):

	g3 = 6
	h0 = x
	paths = []
	try:
		if h0 < 5:
			g3 = g3+g3
			paths.append(1)
		else:
			h0 = h0/x
			x = 1-x
			h0 = x-x
			paths.append(2)
		if x > 5:
			x = x-5
			h0 = 2/h0
			h0 = 0*h0
			paths.append(3)
		else:
			g3 = x+x
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