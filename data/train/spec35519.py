import numpy as np 

def function(x):

	z2 = x
	c7 = x
	paths = []
	try:
		if x > 2:
			x = x-6
			paths.append(1)
		else:
			z2 = x-2
			z2 = 6+4
			paths.append(2)
		if x < 0:
			x = x*c7
			c7 = c7+2
			x = x-x
			paths.append(3)
		else:
			z2 = z2*z2
			x = x-0
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))