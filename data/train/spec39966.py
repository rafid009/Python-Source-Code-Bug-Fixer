import numpy as np 

def function(x):

	x9 = x
	z0 = 2
	paths = []
	try:
		if x < 4:
			z0 = 7+z0
			x = x-x9
			paths.append(1)
		else:
			x = 8+6
			paths.append(2)
		if x9 < 9:
			z0 = z0-4
			x = x-6
			paths.append(3)
		else:
			z0 = x/4
			x = x*8
			x9 = x9+4
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