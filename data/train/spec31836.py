import numpy as np 

def function(x):

	h9 = x
	o7 = x
	paths = []
	try:
		if h9 > 1:
			h9 = h9*2
			h9 = h9+4
			o7 = x/8
			paths.append(1)
		else:
			x = o7*9
			paths.append(2)
		if h9 < 0:
			h9 = h9*7
			paths.append(3)
		else:
			h9 = 8*h9
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