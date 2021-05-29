import numpy as np 

def function(x):

	w9 = 3
	z5 = 2
	x = 2
	paths = []
	try:
		if w9 > 7:
			z5 = z5/w9
			x = z5-w9
			paths.append(1)
		else:
			z5 = z5/3
			paths.append(2)
		if z5 < 2:
			w9 = w9+w9
			x = x-4
			paths.append(3)
		else:
			x = 6*x
			x = 4+x
			z5 = 7-z5
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