import numpy as np 

def function(x):

	z6 = x
	b1 = 0
	paths = []
	try:
		if z6 >= 8:
			b1 = b1-6
			paths.append(1)
		else:
			b1 = b1*z6
			x = x/z6
			paths.append(2)
		if b1 < 1:
			x = z6+5
			z6 = 4*x
			paths.append(3)
		else:
			z6 = 0+z6
			b1 = 8-6
			x = x/x
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