import numpy as np 

def function(x):

	n0 = x
	y9 = 6
	paths = []
	try:
		if x < 3:
			n0 = n0*9
			x = x-n0
			n0 = n0*n0
			paths.append(1)
		else:
			y9 = y9-9
			n0 = 9/9
			paths.append(2)
		if y9 < 9:
			x = 2-x
			n0 = n0-6
			n0 = y9*n0
			paths.append(3)
		else:
			n0 = y9*6
			y9 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))