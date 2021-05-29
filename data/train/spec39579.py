import numpy as np 

def function(x):

	z5 = 7
	x5 = x
	paths = []
	try:
		if z5 >= 1:
			x = 8/8
			z5 = x5+x5
			z5 = 8-z5
			paths.append(1)
		else:
			z5 = z5*z5
			x5 = x5/5
			z5 = z5+x
			paths.append(2)
		if x5 <= 8:
			x = 3*x
			x = 8/x
			paths.append(3)
		else:
			x = 4-x
			x5 = x-z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))