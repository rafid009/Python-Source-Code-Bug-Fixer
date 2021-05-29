import numpy as np 

def function(x):

	j4 = 5
	z5 = 7
	x = 3
	paths = []
	try:
		if z5 <= 7:
			x = x-4
			paths.append(1)
		else:
			x = 7+3
			z5 = 1+8
			j4 = x*j4
			paths.append(2)
		if z5 <= 2:
			j4 = j4/z5
			z5 = z5/2
			z5 = x+z5
			paths.append(3)
		else:
			z5 = z5*z5
			z5 = x-z5
			j4 = 5-j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))