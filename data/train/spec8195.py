import numpy as np 

def function(x):

	o7 = 1
	y9 = 5
	paths = []
	try:
		if o7 > 5:
			x = o7-7
			x = x-2
			paths.append(1)
		else:
			y9 = 5+y9
			y9 = 2*y9
			paths.append(2)
		if o7 <= 8:
			x = x*6
			paths.append(3)
		else:
			o7 = o7-6
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