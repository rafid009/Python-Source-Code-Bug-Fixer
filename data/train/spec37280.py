import numpy as np 

def function(x):

	y9 = x
	w4 = x
	paths = []
	try:
		if w4 > 1:
			y9 = y9/3
			x = x-x
			paths.append(1)
		else:
			w4 = 1/y9
			y9 = y9-6
			paths.append(2)
		if y9 > 0:
			w4 = 2/6
			y9 = y9/y9
			w4 = y9+7
			paths.append(3)
		else:
			w4 = w4/6
			y9 = y9/5
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))