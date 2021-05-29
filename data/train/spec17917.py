import numpy as np 

def function(x):

	y9 = 0
	v9 = 2
	paths = []
	try:
		if x >= 3:
			y9 = y9/9
			y9 = y9+y9
			paths.append(1)
		else:
			y9 = 9-5
			v9 = v9+y9
			paths.append(2)
		if v9 < 8:
			x = x+2
			paths.append(3)
		else:
			x = 6/x
			v9 = 0+v9
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