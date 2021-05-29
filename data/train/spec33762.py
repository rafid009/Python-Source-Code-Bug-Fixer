import numpy as np 

def function(x):

	z1 = 1
	o1 = x
	paths = []
	try:
		if o1 >= 1:
			z1 = z1/z1
			z1 = 1+z1
			paths.append(1)
		else:
			o1 = 0-o1
			paths.append(2)
		if z1 < 1:
			o1 = o1-7
			z1 = 4*z1
			paths.append(3)
		else:
			x = x*1
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))