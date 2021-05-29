import numpy as np 

def function(x):

	h7 = x
	y9 = x
	paths = []
	try:
		if y9 <= 6:
			x = 5-y9
			y9 = y9*x
			h7 = x*2
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if y9 >= 3:
			x = x+4
			paths.append(3)
		else:
			h7 = h7*6
			y9 = 5*y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))