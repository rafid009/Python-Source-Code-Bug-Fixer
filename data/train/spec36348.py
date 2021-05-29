import numpy as np 

def function(x):

	z9 = x
	c2 = 5
	paths = []
	try:
		if x >= 5:
			z9 = z9*9
			x = x/3
			x = z9+z9
			paths.append(1)
		else:
			z9 = x-2
			c2 = 9/c2
			c2 = z9/x
			paths.append(2)
		if c2 >= 2:
			c2 = x*x
			c2 = c2/7
			z9 = 6-z9
			paths.append(3)
		else:
			z9 = z9-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))