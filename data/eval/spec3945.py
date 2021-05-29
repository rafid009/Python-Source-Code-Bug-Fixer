import numpy as np 

def function(x):

	a2 = 0
	y9 = 0
	paths = []
	try:
		if a2 >= 2:
			a2 = x-y9
			x = 1+y9
			a2 = 6/8
			paths.append(1)
		else:
			a2 = 7/8
			y9 = y9-x
			y9 = y9-6
			paths.append(2)
		if a2 >= 5:
			y9 = 3/y9
			paths.append(3)
		else:
			x = x+a2
			y9 = y9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))