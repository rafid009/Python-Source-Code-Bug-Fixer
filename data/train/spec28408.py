import numpy as np 

def function(x):

	b0 = 8
	z6 = x
	paths = []
	try:
		if x > 6:
			b0 = b0+9
			z6 = x/5
			paths.append(1)
		else:
			z6 = 9*z6
			x = x-9
			paths.append(2)
		if x > 7:
			b0 = b0/z6
			paths.append(3)
		else:
			b0 = 2*x
			x = 6-8
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