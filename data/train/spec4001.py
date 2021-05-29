import numpy as np 

def function(x):

	o6 = 9
	y9 = 2
	paths = []
	try:
		if x >= 8:
			y9 = 4/8
			paths.append(1)
		else:
			y9 = y9-x
			y9 = 0/y9
			y9 = o6-y9
			paths.append(2)
		if x >= 0:
			o6 = o6+x
			o6 = o6*4
			o6 = 8-6
			paths.append(3)
		else:
			x = x-3
			y9 = y9*6
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