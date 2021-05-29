import numpy as np 

def function(x):

	x0 = 5
	z5 = x
	paths = []
	try:
		if x0 > 6:
			z5 = z5+x
			x0 = x0-3
			x = x/3
			paths.append(1)
		else:
			z5 = 0/z5
			paths.append(2)
		if x < 8:
			z5 = z5-5
			paths.append(3)
		else:
			x0 = 8*z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))