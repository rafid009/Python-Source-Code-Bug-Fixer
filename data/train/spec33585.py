import numpy as np 

def function(x):

	z8 = x
	b0 = 6
	paths = []
	try:
		if x >= 8:
			x = 8*8
			z8 = 7*z8
			paths.append(1)
		else:
			b0 = z8-3
			x = 4-x
			paths.append(2)
		if b0 > 0:
			z8 = 0-z8
			paths.append(3)
		else:
			b0 = b0+x
			x = 2/4
			z8 = 6*b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))