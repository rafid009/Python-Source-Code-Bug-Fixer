import numpy as np 

def function(x):

	r2 = x
	z8 = x
	paths = []
	try:
		if z8 < 5:
			x = z8/6
			r2 = z8/r2
			r2 = 2*r2
			paths.append(1)
		else:
			z8 = z8-8
			r2 = 0*8
			z8 = 0*0
			paths.append(2)
		if z8 <= 6:
			r2 = r2*z8
			paths.append(3)
		else:
			x = 6*z8
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