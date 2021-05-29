import numpy as np 

def function(x):

	z4 = 3
	z6 = 6
	paths = []
	try:
		if x >= 3:
			z6 = z6-2
			x = z4/z6
			z6 = 8-0
			paths.append(1)
		else:
			x = z4-0
			paths.append(2)
		if z6 < 3:
			z6 = 2/z6
			z4 = 8-z6
			paths.append(3)
		else:
			z6 = z6-8
			x = x+2
			z4 = 5-6
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z6 = z4**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))