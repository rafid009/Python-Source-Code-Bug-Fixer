import numpy as np 

def function(x):

	y9 = x
	a1 = x
	paths = []
	try:
		if x <= 2:
			a1 = a1/1
			paths.append(1)
		else:
			y9 = y9/4
			y9 = 5-x
			paths.append(2)
		if y9 >= 5:
			y9 = 8*y9
			y9 = y9+1
			paths.append(3)
		else:
			x = x-y9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))