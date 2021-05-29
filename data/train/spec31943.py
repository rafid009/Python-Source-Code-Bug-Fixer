import numpy as np 

def function(x):

	q8 = 0
	z0 = x
	paths = []
	try:
		if z0 > 1:
			z0 = 6/z0
			q8 = q8*6
			q8 = q8*0
			paths.append(1)
		else:
			q8 = 2*q8
			x = 4+x
			paths.append(2)
		if x > 6:
			z0 = 6*z0
			paths.append(3)
		else:
			q8 = q8+7
			q8 = 0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))