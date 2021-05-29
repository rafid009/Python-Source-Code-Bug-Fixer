import numpy as np 

def function(x):

	y9 = 7
	u3 = 7
	paths = []
	try:
		if x >= 0:
			x = y9-x
			paths.append(1)
		else:
			y9 = 5-y9
			paths.append(2)
		if y9 > 8:
			u3 = u3+3
			y9 = 2/y9
			paths.append(3)
		else:
			u3 = u3+2
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