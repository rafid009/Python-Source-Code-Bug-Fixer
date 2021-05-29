import numpy as np 

def function(x):

	z7 = x
	p2 = x
	paths = []
	try:
		if z7 <= 2:
			p2 = p2-3
			z7 = z7-5
			z7 = 0-z7
			paths.append(1)
		else:
			z7 = z7/3
			z7 = z7/3
			paths.append(2)
		if z7 <= 0:
			z7 = z7-6
			z7 = 1*z7
			x = 5/z7
			paths.append(3)
		else:
			p2 = 3*z7
			z7 = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))