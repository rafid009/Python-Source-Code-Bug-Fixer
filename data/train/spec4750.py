import numpy as np 

def function(x):

	w7 = 9
	h9 = x
	paths = []
	try:
		if h9 < 5:
			w7 = 6*w7
			x = x-3
			w7 = w7+8
			paths.append(1)
		else:
			x = x*4
			x = x+3
			paths.append(2)
		if h9 < 5:
			h9 = 7*h9
			paths.append(3)
		else:
			x = x+7
			h9 = h9+x
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