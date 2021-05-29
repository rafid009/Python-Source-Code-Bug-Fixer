import numpy as np 

def function(x):

	z0 = 8
	a6 = 8
	paths = []
	try:
		if x > 9:
			a6 = a6-0
			x = x/8
			paths.append(1)
		else:
			z0 = z0*z0
			a6 = a6+a6
			paths.append(2)
		if a6 < 3:
			a6 = a6-7
			paths.append(3)
		else:
			x = x*2
			a6 = 6+8
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