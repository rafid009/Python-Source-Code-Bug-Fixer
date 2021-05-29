import numpy as np 

def function(x):

	y9 = x
	o6 = 1
	paths = []
	try:
		if o6 < 4:
			o6 = 0/y9
			x = x/5
			x = y9+7
			paths.append(1)
		else:
			y9 = 1/9
			paths.append(2)
		if x <= 2:
			y9 = y9*1
			paths.append(3)
		else:
			x = 6-3
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