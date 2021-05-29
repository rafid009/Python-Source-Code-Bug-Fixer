import numpy as np 

def function(x):

	z7 = 5
	z0 = x
	paths = []
	try:
		if z7 <= 7:
			z7 = 1*5
			x = x+z7
			z0 = z0-z7
			paths.append(1)
		else:
			x = 1+4
			z7 = 5/z7
			z0 = z7*3
			paths.append(2)
		if x > 5:
			z0 = x-2
			x = x/1
			paths.append(3)
		else:
			x = z7*1
			x = z0*z7
			z0 = z0/4
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