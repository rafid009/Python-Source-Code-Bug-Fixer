import numpy as np 

def function(x):

	z8 = 8
	n8 = x
	x = x
	paths = []
	try:
		if z8 < 0:
			x = 9+3
			paths.append(1)
		else:
			z8 = z8-0
			z8 = x-6
			x = x*z8
			paths.append(2)
		if x > 8:
			n8 = n8/8
			paths.append(3)
		else:
			z8 = 8+3
			x = x*n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		z8 = n8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))