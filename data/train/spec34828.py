import numpy as np 

def function(x):

	e0 = 7
	y9 = 1
	paths = []
	try:
		if y9 <= 6:
			y9 = 9+y9
			paths.append(1)
		else:
			x = x-x
			y9 = y9*9
			y9 = 7/6
			paths.append(2)
		if e0 <= 8:
			x = x/3
			paths.append(3)
		else:
			y9 = y9*6
			e0 = e0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))