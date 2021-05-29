import numpy as np 

def function(x):

	p3 = 9
	z9 = x
	paths = []
	try:
		if z9 > 2:
			z9 = 9*6
			x = 0-7
			paths.append(1)
		else:
			z9 = z9-3
			z9 = z9*7
			z9 = z9/5
			paths.append(2)
		if z9 < 4:
			z9 = 8*z9
			z9 = 9+z9
			paths.append(3)
		else:
			p3 = 1/p3
			p3 = z9/z9
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))