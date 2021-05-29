import numpy as np 

def function(x):

	d1 = 3
	y9 = x
	paths = []
	try:
		if x <= 1:
			d1 = 4*9
			d1 = x/d1
			d1 = 9/d1
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if d1 >= 1:
			y9 = 2*y9
			y9 = y9+7
			paths.append(3)
		else:
			d1 = 9/5
			y9 = y9-4
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