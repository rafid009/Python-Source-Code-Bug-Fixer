import numpy as np 

def function(x):

	z9 = x
	q8 = 5
	paths = []
	try:
		if x >= 1:
			z9 = z9+0
			q8 = q8-9
			paths.append(1)
		else:
			z9 = q8/2
			z9 = 1+z9
			q8 = z9*q8
			paths.append(2)
		if q8 < 7:
			x = 0-x
			paths.append(3)
		else:
			q8 = q8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))