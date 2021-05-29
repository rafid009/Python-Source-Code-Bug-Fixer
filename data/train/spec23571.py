import numpy as np 

def function(x):

	a9 = x
	y9 = x
	paths = []
	try:
		if x <= 8:
			y9 = a9+7
			paths.append(1)
		else:
			a9 = 4*x
			paths.append(2)
		if x <= 2:
			x = y9+x
			y9 = y9/6
			a9 = a9-y9
			paths.append(3)
		else:
			a9 = 2/x
			y9 = 9*y9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))