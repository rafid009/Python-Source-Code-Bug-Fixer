import numpy as np 

def function(x):

	z8 = 8
	r9 = 3
	paths = []
	try:
		if z8 <= 7:
			z8 = 2/z8
			z8 = 3+r9
			z8 = 6*z8
			paths.append(1)
		else:
			r9 = r9+3
			x = x/9
			z8 = 6/4
			paths.append(2)
		if x > 4:
			r9 = r9*z8
			z8 = r9/z8
			r9 = r9/1
			paths.append(3)
		else:
			z8 = 3-z8
			x = x/8
			x = z8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))