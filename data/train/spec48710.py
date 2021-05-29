import numpy as np 

def function(x):

	z9 = 4
	c7 = x
	paths = []
	try:
		if x <= 3:
			c7 = 8-c7
			paths.append(1)
		else:
			x = 8-x
			z9 = z9+4
			paths.append(2)
		if c7 < 8:
			z9 = z9-c7
			c7 = c7-z9
			z9 = z9*5
			paths.append(3)
		else:
			z9 = c7+z9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		c7 = z9**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))