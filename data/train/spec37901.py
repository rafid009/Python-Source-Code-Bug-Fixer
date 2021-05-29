import numpy as np 

def function(x):

	w4 = x
	y9 = 5
	x = x
	paths = []
	try:
		if x > 5:
			x = 1+3
			y9 = 2/y9
			paths.append(1)
		else:
			y9 = w4-y9
			paths.append(2)
		if w4 > 9:
			x = x*9
			y9 = y9+y9
			y9 = x*y9
			paths.append(3)
		else:
			y9 = y9/1
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))