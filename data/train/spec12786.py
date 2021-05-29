import numpy as np 

def function(x):

	l0 = 2
	y9 = x
	paths = []
	try:
		if l0 >= 8:
			l0 = 3*l0
			paths.append(1)
		else:
			x = 9+y9
			y9 = y9/9
			paths.append(2)
		if l0 >= 6:
			l0 = l0/l0
			l0 = l0-x
			paths.append(3)
		else:
			y9 = l0-4
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