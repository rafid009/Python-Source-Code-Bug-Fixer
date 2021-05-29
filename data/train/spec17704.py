import numpy as np 

def function(x):

	z6 = x
	i1 = 6
	paths = []
	try:
		if x < 7:
			i1 = i1+z6
			i1 = i1-7
			paths.append(1)
		else:
			i1 = i1-8
			x = i1/x
			paths.append(2)
		if z6 <= 8:
			z6 = x+z6
			z6 = x/z6
			paths.append(3)
		else:
			z6 = i1*x
			x = 9-x
			z6 = 9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))