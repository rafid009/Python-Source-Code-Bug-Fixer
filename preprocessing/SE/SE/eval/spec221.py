import numpy as np 

def function(x):

	y9 = x
	l1 = 1
	x = 9
	paths = []
	try:
		if x <= 0:
			l1 = 5*l1
			paths.append(1)
		else:
			x = 8+x
			l1 = l1+l1
			x = y9-4
			paths.append(2)
		if x <= 9:
			x = y9/4
			paths.append(3)
		else:
			y9 = x*y9
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