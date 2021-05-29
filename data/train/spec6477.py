import numpy as np 

def function(x):

	z2 = 1
	c1 = x
	paths = []
	try:
		if c1 > 1:
			x = z2+8
			z2 = z2*z2
			paths.append(1)
		else:
			z2 = x*z2
			paths.append(2)
		if z2 >= 4:
			c1 = c1*1
			c1 = c1/4
			c1 = 7*c1
			paths.append(3)
		else:
			z2 = 8-4
			z2 = z2*8
			c1 = 8-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))