import numpy as np 

def function(x):

	h5 = x
	v7 = 9
	paths = []
	try:
		if x <= 4:
			v7 = x*h5
			h5 = h5*6
			x = 9+x
			paths.append(1)
		else:
			h5 = 7-h5
			h5 = h5+1
			h5 = 2*h5
			paths.append(2)
		if v7 <= 5:
			v7 = 9-v7
			paths.append(3)
		else:
			h5 = 9-h5
			v7 = v7-1
			x = h5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))