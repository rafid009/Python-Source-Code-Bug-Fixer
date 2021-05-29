import numpy as np 

def function(x):

	l7 = x
	y9 = 8
	paths = []
	try:
		if l7 < 9:
			y9 = y9+6
			l7 = y9*5
			l7 = l7+3
			paths.append(1)
		else:
			x = x/2
			y9 = 2*l7
			paths.append(2)
		if x >= 5:
			y9 = y9+8
			y9 = 4*y9
			paths.append(3)
		else:
			y9 = 6+7
			l7 = l7-1
			x = 4*x
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