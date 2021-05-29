import numpy as np 

def function(x):

	z8 = x
	p7 = 3
	paths = []
	try:
		if z8 > 4:
			x = z8-4
			paths.append(1)
		else:
			p7 = 6/p7
			p7 = p7+6
			p7 = 4-p7
			paths.append(2)
		if x >= 9:
			z8 = z8*5
			x = x-4
			paths.append(3)
		else:
			z8 = z8-1
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		z8 = p7**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))