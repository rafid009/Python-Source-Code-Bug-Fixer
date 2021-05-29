import numpy as np 

def function(x):

	z6 = x
	c0 = x
	paths = []
	try:
		if z6 >= 7:
			c0 = c0*2
			z6 = 5+z6
			c0 = 5+4
			paths.append(1)
		else:
			z6 = z6-3
			paths.append(2)
		if z6 >= 8:
			z6 = 0*x
			z6 = 1*z6
			z6 = z6*6
			paths.append(3)
		else:
			c0 = 0*4
			c0 = x-7
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))