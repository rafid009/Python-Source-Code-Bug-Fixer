import numpy as np 

def function(x):

	z8 = 3
	n2 = 2
	paths = []
	try:
		if n2 >= 9:
			x = 8+x
			z8 = 1+3
			paths.append(1)
		else:
			n2 = 2+n2
			n2 = n2-7
			paths.append(2)
		if z8 > 1:
			z8 = z8-2
			x = x+z8
			paths.append(3)
		else:
			z8 = z8+n2
			z8 = z8-x
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))