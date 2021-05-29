import numpy as np 

def function(x):

	n3 = 4
	z5 = x
	paths = []
	try:
		if x < 5:
			z5 = z5*z5
			z5 = 9+x
			paths.append(1)
		else:
			z5 = 3+z5
			paths.append(2)
		if z5 < 2:
			n3 = x+n3
			n3 = n3/z5
			x = x+3
			paths.append(3)
		else:
			x = x/3
			n3 = 6*n3
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