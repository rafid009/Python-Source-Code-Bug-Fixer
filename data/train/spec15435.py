import numpy as np 

def function(x):

	p1 = 9
	z0 = 0
	paths = []
	try:
		if x <= 3:
			z0 = 9-2
			z0 = z0/8
			paths.append(1)
		else:
			z0 = 6+z0
			x = x*x
			paths.append(2)
		if x <= 6:
			z0 = p1+1
			paths.append(3)
		else:
			z0 = z0+7
			p1 = p1*z0
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