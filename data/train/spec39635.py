import numpy as np 

def function(x):

	n8 = x
	z8 = 9
	x = 2
	paths = []
	try:
		if z8 <= 9:
			z8 = 0-n8
			x = 1/x
			n8 = x+n8
			paths.append(1)
		else:
			x = n8/n8
			x = x+x
			x = z8*x
			paths.append(2)
		if x >= 9:
			n8 = 2*n8
			z8 = z8+5
			paths.append(3)
		else:
			z8 = z8-6
			z8 = 3+x
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