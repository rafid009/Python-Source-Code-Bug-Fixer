import numpy as np 

def function(x):

	z0 = 5
	a1 = 6
	paths = []
	try:
		if z0 >= 3:
			a1 = a1-6
			x = x-6
			a1 = 5*3
			paths.append(1)
		else:
			a1 = a1*4
			a1 = 2/5
			z0 = 3/6
			paths.append(2)
		if x >= 4:
			z0 = 3*z0
			z0 = 2*a1
			paths.append(3)
		else:
			z0 = z0*2
			x = x-z0
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