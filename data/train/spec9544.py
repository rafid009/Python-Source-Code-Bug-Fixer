import numpy as np 

def function(x):

	u0 = x
	z1 = x
	paths = []
	try:
		if z1 < 8:
			u0 = u0*4
			x = x-3
			paths.append(1)
		else:
			z1 = 8-u0
			paths.append(2)
		if u0 > 2:
			x = x-x
			u0 = u0-z1
			z1 = 6/z1
			paths.append(3)
		else:
			x = u0+z1
			z1 = z1-4
			z1 = 1+7
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))