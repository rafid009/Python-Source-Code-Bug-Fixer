import numpy as np 

def function(x):

	g5 = x
	h0 = x
	paths = []
	try:
		if h0 < 3:
			g5 = g5-h0
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if x <= 0:
			h0 = h0/9
			h0 = h0*3
			x = x+0
			paths.append(3)
		else:
			x = x*3
			g5 = 3+x
			x = h0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))