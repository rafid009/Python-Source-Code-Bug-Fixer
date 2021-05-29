import numpy as np 

def function(x):

	e3 = x
	z8 = 5
	paths = []
	try:
		if x >= 5:
			e3 = x/7
			paths.append(1)
		else:
			z8 = z8-5
			z8 = 8*1
			paths.append(2)
		if z8 <= 0:
			x = x+x
			paths.append(3)
		else:
			e3 = 2*6
			z8 = 9/z8
			z8 = 0*z8
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