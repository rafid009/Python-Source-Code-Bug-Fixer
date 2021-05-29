import numpy as np 

def function(x):

	z2 = 2
	c1 = x
	paths = []
	try:
		if x >= 1:
			z2 = c1+9
			z2 = 9+0
			x = 6-x
			paths.append(1)
		else:
			c1 = 1-5
			c1 = 3/c1
			paths.append(2)
		if z2 < 3:
			c1 = x-8
			z2 = z2-x
			z2 = 5/x
			paths.append(3)
		else:
			x = x-4
			x = 9-1
			z2 = 5*z2
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))