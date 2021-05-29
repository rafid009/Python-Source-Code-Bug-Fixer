import numpy as np 

def function(x):

	z5 = 1
	w5 = x
	paths = []
	try:
		if x >= 0:
			w5 = 0-7
			paths.append(1)
		else:
			z5 = z5+w5
			paths.append(2)
		if z5 < 3:
			w5 = w5-0
			x = 7/x
			z5 = z5*z5
			paths.append(3)
		else:
			w5 = 0*w5
			z5 = 2-z5
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