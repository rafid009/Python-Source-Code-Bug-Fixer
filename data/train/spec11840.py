import numpy as np 

def function(x):

	a3 = x
	z5 = x
	x = x
	paths = []
	try:
		if z5 <= 4:
			a3 = 2*a3
			z5 = z5*a3
			z5 = x-z5
			paths.append(1)
		else:
			z5 = z5/8
			z5 = x*a3
			paths.append(2)
		if x >= 5:
			a3 = 8-x
			a3 = 9/a3
			paths.append(3)
		else:
			x = x+6
			x = z5/2
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