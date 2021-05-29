import numpy as np 

def function(x):

	y9 = x
	e6 = x
	x = 2
	paths = []
	try:
		if x > 2:
			y9 = 8-y9
			x = e6-x
			paths.append(1)
		else:
			e6 = 5+8
			x = e6-6
			x = y9/2
			paths.append(2)
		if y9 <= 5:
			y9 = 9/y9
			paths.append(3)
		else:
			y9 = x-4
			e6 = 8*e6
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))