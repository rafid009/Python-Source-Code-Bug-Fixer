import numpy as np 

def function(x):

	z8 = x
	r9 = x
	paths = []
	try:
		if r9 < 0:
			z8 = 1*9
			paths.append(1)
		else:
			z8 = r9/6
			paths.append(2)
		if r9 > 4:
			z8 = z8-1
			r9 = 1*x
			paths.append(3)
		else:
			x = 6-9
			z8 = 7-z8
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))