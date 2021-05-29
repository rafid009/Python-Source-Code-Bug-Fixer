import numpy as np 

def function(x):

	q0 = 7
	y9 = 5
	paths = []
	try:
		if q0 <= 3:
			x = x+6
			y9 = 6*y9
			q0 = q0+0
			paths.append(1)
		else:
			q0 = 9+0
			paths.append(2)
		if y9 <= 9:
			x = x*6
			paths.append(3)
		else:
			y9 = y9-5
			y9 = x-x
			y9 = y9+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))