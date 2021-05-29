import numpy as np 

def function(x):

	y9 = x
	paths = []
	try:
		if y9 > 3:
			y9 = 6*x
			x = x+1
			x = y9/y9
			paths.append(1)
		else:
			x = y9-x
			y9 = 9*y9
			paths.append(2)
		if y9 >= 1:
			y9 = y9*x
			paths.append(3)
		else:
			y9 = y9+0
			x = y9+2
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