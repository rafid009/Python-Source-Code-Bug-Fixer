import numpy as np 

def function(x):

	h6 = 8
	k0 = 4
	paths = []
	try:
		if h6 < 8:
			h6 = 3*5
			h6 = h6+1
			paths.append(1)
		else:
			k0 = 1-4
			paths.append(2)
		if k0 < 4:
			x = 4/4
			x = 3/k0
			paths.append(3)
		else:
			h6 = h6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))