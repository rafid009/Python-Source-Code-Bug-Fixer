import numpy as np 

def function(x):

	y9 = 1
	h8 = x
	paths = []
	try:
		if x <= 3:
			h8 = x*7
			h8 = h8/h8
			paths.append(1)
		else:
			h8 = 3-h8
			x = y9*y9
			paths.append(2)
		if h8 <= 2:
			y9 = y9*0
			h8 = 0*h8
			y9 = x+y9
			paths.append(3)
		else:
			y9 = y9-2
			h8 = h8/h8
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		h8 = y9**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))