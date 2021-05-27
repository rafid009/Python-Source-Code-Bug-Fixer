import numpy as np 

def function(x):

	y9 = 3
	y7 = x
	paths = []
	try:
		if x > 3:
			y9 = x+9
			y7 = 1-y7
			y9 = y9+5
			paths.append(1)
		else:
			y9 = 7-x
			paths.append(2)
		if y9 <= 8:
			x = y9*x
			y9 = y9-7
			y7 = 0+y7
			paths.append(3)
		else:
			x = x/3
			y9 = 0-7
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