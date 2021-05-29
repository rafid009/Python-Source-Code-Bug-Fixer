import numpy as np 

def function(x):

	l8 = 6
	z6 = x
	paths = []
	try:
		if x <= 6:
			l8 = 3*l8
			paths.append(1)
		else:
			l8 = l8/7
			z6 = l8-z6
			paths.append(2)
		if x < 3:
			z6 = z6*3
			z6 = z6/1
			paths.append(3)
		else:
			z6 = z6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))