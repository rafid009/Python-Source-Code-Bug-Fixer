import numpy as np 

def function(x):

	c0 = 4
	z4 = x
	paths = []
	try:
		if z4 > 3:
			z4 = z4*z4
			paths.append(1)
		else:
			c0 = 5*9
			paths.append(2)
		if z4 >= 9:
			c0 = 9*8
			z4 = 5+c0
			paths.append(3)
		else:
			c0 = c0/x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))