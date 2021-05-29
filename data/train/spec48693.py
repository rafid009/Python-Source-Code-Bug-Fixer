import numpy as np 

def function(x):

	z8 = x
	f1 = 0
	paths = []
	try:
		if z8 >= 1:
			x = 6*x
			z8 = z8-f1
			paths.append(1)
		else:
			f1 = f1*f1
			paths.append(2)
		if x > 0:
			f1 = 9*z8
			paths.append(3)
		else:
			z8 = z8-x
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