import numpy as np 

def function(x):

	h4 = 8
	y9 = x
	paths = []
	try:
		if y9 <= 9:
			x = x+1
			y9 = y9-h4
			paths.append(1)
		else:
			y9 = 2/h4
			y9 = y9*3
			paths.append(2)
		if x >= 3:
			y9 = y9-y9
			h4 = y9+y9
			h4 = h4+h4
			paths.append(3)
		else:
			h4 = h4-4
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))