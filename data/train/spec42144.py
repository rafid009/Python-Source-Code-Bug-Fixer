import numpy as np 

def function(x):

	y9 = 9
	d7 = x
	paths = []
	try:
		if y9 > 8:
			y9 = 2/y9
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if y9 <= 0:
			d7 = d7*6
			y9 = 9-y9
			paths.append(3)
		else:
			y9 = y9+d7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))