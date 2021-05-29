import numpy as np 

def function(x):

	f1 = x
	z6 = x
	paths = []
	try:
		if x <= 7:
			z6 = 2/3
			f1 = f1-4
			paths.append(1)
		else:
			z6 = 6*f1
			f1 = f1*x
			z6 = 9/f1
			paths.append(2)
		if x > 1:
			f1 = f1/x
			paths.append(3)
		else:
			z6 = x/1
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