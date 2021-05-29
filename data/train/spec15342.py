import numpy as np 

def function(x):

	z2 = x
	b1 = 4
	paths = []
	try:
		if b1 <= 8:
			z2 = 3+3
			z2 = 6/z2
			paths.append(1)
		else:
			z2 = 0-4
			paths.append(2)
		if z2 > 7:
			z2 = 0-z2
			x = 8/x
			paths.append(3)
		else:
			b1 = 0+b1
			b1 = 6*b1
			z2 = z2+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))