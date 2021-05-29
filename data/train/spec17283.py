import numpy as np 

def function(x):

	k0 = 1
	h3 = 8
	x = x
	paths = []
	try:
		if h3 > 8:
			h3 = h3-9
			paths.append(1)
		else:
			h3 = h3*k0
			x = 8+x
			k0 = 9*6
			paths.append(2)
		if x > 6:
			h3 = 4-h3
			paths.append(3)
		else:
			x = 8*x
			x = x*3
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