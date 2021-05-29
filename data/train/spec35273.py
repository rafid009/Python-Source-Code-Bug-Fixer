import numpy as np 

def function(x):

	c3 = 9
	z2 = x
	paths = []
	try:
		if c3 >= 5:
			x = 6*x
			x = x+5
			c3 = c3/6
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if c3 < 4:
			z2 = z2-5
			paths.append(3)
		else:
			z2 = z2*z2
			x = 7*3
			x = 2*z2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		c3 = z2**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))