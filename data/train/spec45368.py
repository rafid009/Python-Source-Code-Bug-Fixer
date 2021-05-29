import numpy as np 

def function(x):

	z0 = x
	l7 = 2
	paths = []
	try:
		if z0 < 3:
			z0 = x+1
			x = 7-x
			paths.append(1)
		else:
			z0 = x*l7
			x = 0-l7
			x = x+6
			paths.append(2)
		if x < 1:
			z0 = z0*z0
			z0 = 5*z0
			l7 = 8+l7
			paths.append(3)
		else:
			x = 0-z0
			l7 = 7/x
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