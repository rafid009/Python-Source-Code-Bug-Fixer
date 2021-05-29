import numpy as np 

def function(x):

	h5 = x
	g0 = 0
	paths = []
	try:
		if g0 > 7:
			x = 5/x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if g0 > 1:
			h5 = h5-3
			paths.append(3)
		else:
			g0 = g0-7
			h5 = h5-1
			x = x-2
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		h5 = g0**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))