import numpy as np 

def function(x):

	z0 = 1
	x5 = x
	paths = []
	try:
		if x5 > 0:
			x = z0/z0
			paths.append(1)
		else:
			z0 = 5/3
			x5 = z0+x5
			x5 = 5-x5
			paths.append(2)
		if x5 >= 4:
			z0 = z0/3
			z0 = x5/5
			x5 = 1/x
			paths.append(3)
		else:
			x = 2-x
			z0 = 5-8
			x = 4*z0
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))