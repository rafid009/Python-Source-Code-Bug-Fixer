import numpy as np 

def function(x):

	q7 = x
	z8 = 8
	paths = []
	try:
		if q7 < 0:
			z8 = 1*z8
			paths.append(1)
		else:
			z8 = x*z8
			paths.append(2)
		if z8 > 3:
			q7 = q7+8
			x = 8/x
			paths.append(3)
		else:
			q7 = q7*4
			x = 0-5
			q7 = 2*q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))