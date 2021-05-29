import numpy as np 

def function(x):

	d6 = x
	y9 = x
	paths = []
	try:
		if y9 > 2:
			x = x/6
			x = 1-x
			x = 2/8
			paths.append(1)
		else:
			y9 = y9+d6
			y9 = y9*x
			paths.append(2)
		if x <= 4:
			x = 6/x
			paths.append(3)
		else:
			y9 = y9/y9
			x = 6*6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		y9 = d6**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))