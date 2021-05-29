import numpy as np 

def function(x):

	r0 = 3
	z8 = 0
	paths = []
	try:
		if z8 < 3:
			z8 = x-6
			z8 = 2/1
			z8 = z8/z8
			paths.append(1)
		else:
			x = x+2
			z8 = 1+z8
			paths.append(2)
		if z8 >= 0:
			z8 = 4-9
			r0 = r0/6
			paths.append(3)
		else:
			z8 = 0*x
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