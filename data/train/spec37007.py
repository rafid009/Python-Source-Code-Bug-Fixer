import numpy as np 

def function(x):

	n5 = 7
	z8 = x
	paths = []
	try:
		if n5 <= 2:
			x = 3*n5
			x = z8*x
			paths.append(1)
		else:
			z8 = z8+z8
			n5 = 6+n5
			z8 = 0*z8
			paths.append(2)
		if z8 > 2:
			n5 = 1/n5
			paths.append(3)
		else:
			z8 = z8-9
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		n5 = z8**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))