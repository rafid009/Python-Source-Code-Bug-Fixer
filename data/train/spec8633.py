import numpy as np 

def function(x):

	z0 = 3
	l1 = x
	paths = []
	try:
		if x < 8:
			l1 = 2+z0
			x = 9/9
			x = x*2
			paths.append(1)
		else:
			l1 = 0+z0
			z0 = z0/2
			paths.append(2)
		if z0 < 0:
			z0 = 3*9
			l1 = l1-8
			z0 = x-l1
			paths.append(3)
		else:
			x = x*z0
			z0 = z0/x
			x = 3-x
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