import numpy as np 

def function(x):

	a9 = x
	h3 = x
	paths = []
	try:
		if a9 < 8:
			h3 = h3*a9
			paths.append(1)
		else:
			x = x*a9
			x = 7/x
			h3 = h3-8
			paths.append(2)
		if h3 < 8:
			a9 = a9+2
			h3 = h3+3
			h3 = h3-7
			paths.append(3)
		else:
			h3 = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))