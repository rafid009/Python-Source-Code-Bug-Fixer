import numpy as np 

def function(x):

	z1 = 2
	x4 = x
	paths = []
	try:
		if x >= 8:
			x = x-6
			paths.append(1)
		else:
			x4 = 9*x4
			paths.append(2)
		if x4 <= 2:
			z1 = 9-z1
			z1 = 7*4
			z1 = 6*z1
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))