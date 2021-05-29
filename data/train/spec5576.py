import numpy as np 

def function(x):

	z2 = 0
	c9 = 3
	paths = []
	try:
		if x < 3:
			c9 = c9*1
			z2 = 1*z2
			x = 2/x
			paths.append(1)
		else:
			z2 = z2-3
			z2 = z2*c9
			paths.append(2)
		if z2 > 6:
			c9 = 8-8
			c9 = c9+3
			z2 = z2*0
			paths.append(3)
		else:
			c9 = c9*0
			z2 = z2+z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))