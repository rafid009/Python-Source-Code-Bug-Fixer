import numpy as np 

def function(x):

	z0 = x
	r6 = 9
	paths = []
	try:
		if z0 < 6:
			r6 = r6+8
			x = x-5
			z0 = z0*5
			paths.append(1)
		else:
			z0 = 3-z0
			paths.append(2)
		if r6 < 5:
			x = z0/9
			z0 = z0-5
			paths.append(3)
		else:
			r6 = r6*z0
			z0 = 5/z0
			x = r6+1
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