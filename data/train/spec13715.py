import numpy as np 

def function(x):

	e4 = x
	z2 = 1
	paths = []
	try:
		if e4 >= 8:
			z2 = 4/e4
			z2 = x-z2
			z2 = 5+z2
			paths.append(1)
		else:
			z2 = z2-8
			z2 = 1+z2
			paths.append(2)
		if e4 > 9:
			z2 = z2/z2
			x = 8/3
			x = x+z2
			paths.append(3)
		else:
			z2 = 4-z2
			z2 = z2-0
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))