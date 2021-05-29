import numpy as np 

def function(x):

	y9 = x
	h3 = 3
	paths = []
	try:
		if x >= 0:
			x = 3*8
			y9 = 7/y9
			y9 = y9+3
			paths.append(1)
		else:
			h3 = h3/6
			x = x/y9
			paths.append(2)
		if h3 < 0:
			y9 = 6+y9
			y9 = y9*7
			y9 = y9/9
			paths.append(3)
		else:
			x = 8+1
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))