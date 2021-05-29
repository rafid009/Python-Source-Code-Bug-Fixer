import numpy as np 

def function(x):

	z0 = 5
	b9 = x
	paths = []
	try:
		if z0 < 2:
			b9 = b9*8
			z0 = z0+4
			paths.append(1)
		else:
			b9 = z0*b9
			paths.append(2)
		if b9 > 5:
			x = 7-6
			b9 = 7/b9
			x = b9*3
			paths.append(3)
		else:
			z0 = z0+z0
			z0 = x-z0
			x = x-b9
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))