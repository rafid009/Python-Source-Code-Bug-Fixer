import numpy as np 

def function(x):

	z1 = 8
	l2 = x
	paths = []
	try:
		if x <= 3:
			l2 = 9-l2
			paths.append(1)
		else:
			l2 = z1-z1
			z1 = 3/z1
			z1 = 3*z1
			paths.append(2)
		if x >= 8:
			l2 = l2-l2
			x = 6*x
			l2 = 6/z1
			paths.append(3)
		else:
			l2 = l2*2
			z1 = 3*z1
			z1 = z1/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))