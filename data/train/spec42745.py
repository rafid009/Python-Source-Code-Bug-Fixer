import numpy as np 

def function(x):

	z0 = x
	b4 = 2
	paths = []
	try:
		if z0 >= 6:
			x = 3+x
			b4 = x/7
			z0 = 4+z0
			paths.append(1)
		else:
			x = x*b4
			z0 = x-6
			paths.append(2)
		if b4 <= 2:
			b4 = b4/z0
			paths.append(3)
		else:
			z0 = z0+x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))