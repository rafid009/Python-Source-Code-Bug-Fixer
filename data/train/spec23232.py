import numpy as np 

def function(x):

	y6 = x
	h2 = 2
	paths = []
	try:
		if y6 < 0:
			h2 = h2-x
			x = 9+x
			paths.append(1)
		else:
			h2 = h2/y6
			paths.append(2)
		if x >= 5:
			h2 = 5*4
			paths.append(3)
		else:
			h2 = 1-8
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))