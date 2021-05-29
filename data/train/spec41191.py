import numpy as np 

def function(x):

	h0 = x
	g9 = 3
	paths = []
	try:
		if g9 <= 2:
			g9 = g9/x
			g9 = 5/2
			h0 = h0+g9
			paths.append(1)
		else:
			g9 = 2*x
			g9 = 3+g9
			paths.append(2)
		if x < 6:
			h0 = 4+9
			x = x-5
			paths.append(3)
		else:
			x = 8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))