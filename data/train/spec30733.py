import numpy as np 

def function(x):

	y9 = 5
	x8 = x
	paths = []
	try:
		if x >= 8:
			x8 = 6-x8
			x = 9-x
			x = x/3
			paths.append(1)
		else:
			x8 = x8*6
			paths.append(2)
		if x <= 9:
			y9 = 0-y9
			x = y9*6
			paths.append(3)
		else:
			x8 = x8-x8
			y9 = 6+x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		y9 = x8**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))