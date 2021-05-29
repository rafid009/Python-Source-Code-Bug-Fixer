import numpy as np 

def function(x):

	a8 = 3
	z9 = 0
	paths = []
	try:
		if x >= 7:
			a8 = a8+0
			z9 = z9-4
			z9 = 8*z9
			paths.append(1)
		else:
			z9 = 5-z9
			paths.append(2)
		if a8 >= 0:
			a8 = 8-a8
			paths.append(3)
		else:
			a8 = 9-a8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))