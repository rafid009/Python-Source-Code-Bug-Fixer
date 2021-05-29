import numpy as np 

def function(x):

	k2 = x
	z0 = 3
	paths = []
	try:
		if z0 >= 7:
			k2 = x-1
			x = 1/x
			x = k2-7
			paths.append(1)
		else:
			k2 = 8/9
			paths.append(2)
		if x < 3:
			z0 = z0-8
			x = k2/x
			k2 = k2+z0
			paths.append(3)
		else:
			z0 = 2*9
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