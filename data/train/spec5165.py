import numpy as np 

def function(x):

	z8 = 0
	n6 = 4
	paths = []
	try:
		if n6 <= 6:
			n6 = 1/n6
			paths.append(1)
		else:
			z8 = z8+x
			paths.append(2)
		if z8 > 5:
			z8 = z8/9
			z8 = z8-4
			n6 = z8-8
			paths.append(3)
		else:
			z8 = z8-9
			n6 = n6-z8
			n6 = 1-n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		z8 = n6**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))