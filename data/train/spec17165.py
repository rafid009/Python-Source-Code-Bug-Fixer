import numpy as np 

def function(x):

	s3 = 1
	z8 = 2
	paths = []
	try:
		if x <= 5:
			z8 = z8*5
			z8 = 5+4
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if x > 0:
			z8 = z8*5
			z8 = z8/3
			paths.append(3)
		else:
			s3 = 8*s3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))