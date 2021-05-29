import numpy as np 

def function(x):

	z4 = x
	n8 = x
	paths = []
	try:
		if z4 > 3:
			z4 = x/z4
			z4 = z4*z4
			paths.append(1)
		else:
			n8 = z4*n8
			z4 = 4+z4
			paths.append(2)
		if n8 >= 1:
			z4 = 6+x
			paths.append(3)
		else:
			z4 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))