import numpy as np 

def function(x):

	z9 = x
	c5 = 8
	paths = []
	try:
		if z9 >= 8:
			z9 = 4-1
			z9 = z9-c5
			c5 = c5*2
			paths.append(1)
		else:
			z9 = z9-c5
			c5 = x*1
			paths.append(2)
		if c5 <= 0:
			c5 = x+c5
			c5 = 0*c5
			z9 = 0*z9
			paths.append(3)
		else:
			c5 = x-z9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))