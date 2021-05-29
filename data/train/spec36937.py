import numpy as np 

def function(x):

	w4 = x
	y9 = x
	paths = []
	try:
		if y9 > 4:
			x = 2*7
			paths.append(1)
		else:
			x = 6*9
			x = 5/x
			x = x*9
			paths.append(2)
		if x <= 4:
			y9 = y9+8
			y9 = y9-8
			x = x-y9
			paths.append(3)
		else:
			x = w4-x
			y9 = 1*y9
			y9 = 5/2
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