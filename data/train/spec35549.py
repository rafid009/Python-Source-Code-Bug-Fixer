import numpy as np 

def function(x):

	z9 = 2
	n3 = x
	paths = []
	try:
		if x >= 2:
			z9 = 0+z9
			paths.append(1)
		else:
			z9 = 8+n3
			z9 = 9+n3
			paths.append(2)
		if z9 < 2:
			n3 = n3-8
			n3 = x-n3
			paths.append(3)
		else:
			x = x+6
			n3 = 1-4
			z9 = z9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))