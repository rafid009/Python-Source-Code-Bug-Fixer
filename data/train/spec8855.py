import numpy as np 

def function(x):

	e0 = x
	z8 = 4
	paths = []
	try:
		if x > 2:
			e0 = e0/9
			z8 = z8+3
			paths.append(1)
		else:
			z8 = e0*z8
			e0 = 7*e0
			e0 = z8+e0
			paths.append(2)
		if x > 8:
			e0 = 7/e0
			x = z8*6
			paths.append(3)
		else:
			x = x+x
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