import numpy as np 

def function(x):

	h9 = 6
	g6 = 9
	paths = []
	try:
		if g6 >= 8:
			g6 = g6+h9
			x = x*9
			h9 = 5+h9
			paths.append(1)
		else:
			h9 = 3/5
			h9 = h9/5
			h9 = h9+h9
			paths.append(2)
		if h9 > 1:
			h9 = 5+h9
			paths.append(3)
		else:
			h9 = h9/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))