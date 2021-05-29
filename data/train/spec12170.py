import numpy as np 

def function(x):

	z1 = x
	a8 = 6
	x = x
	paths = []
	try:
		if x <= 0:
			a8 = a8/a8
			z1 = 2+z1
			paths.append(1)
		else:
			z1 = a8*6
			paths.append(2)
		if z1 > 2:
			a8 = 1*6
			z1 = a8/x
			paths.append(3)
		else:
			a8 = 0-2
			z1 = x-z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))