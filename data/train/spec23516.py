import numpy as np 

def function(x):

	a2 = 3
	z5 = 5
	paths = []
	try:
		if x < 8:
			a2 = z5/a2
			a2 = 9/a2
			a2 = 2*a2
			paths.append(1)
		else:
			a2 = 9/a2
			a2 = a2/9
			z5 = z5+6
			paths.append(2)
		if x < 3:
			z5 = 2-a2
			paths.append(3)
		else:
			z5 = z5*z5
			x = 0-x
			x = 2/x
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