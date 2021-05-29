import numpy as np 

def function(x):

	z6 = x
	a4 = x
	paths = []
	try:
		if x <= 5:
			a4 = 9/z6
			z6 = z6/z6
			paths.append(1)
		else:
			x = 5/x
			a4 = a4-z6
			paths.append(2)
		if a4 > 4:
			x = x*x
			paths.append(3)
		else:
			a4 = 5-z6
			z6 = 7-z6
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