import numpy as np 

def function(x):

	h5 = 2
	y9 = x
	paths = []
	try:
		if x <= 2:
			x = x-0
			paths.append(1)
		else:
			h5 = h5*h5
			h5 = h5-0
			y9 = y9+y9
			paths.append(2)
		if y9 < 7:
			y9 = 8/y9
			h5 = y9/7
			paths.append(3)
		else:
			y9 = 2/3
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))