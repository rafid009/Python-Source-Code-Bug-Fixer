import numpy as np 

def function(x):

	z2 = 9
	c6 = 7
	paths = []
	try:
		if x < 8:
			z2 = z2/x
			x = 9*0
			paths.append(1)
		else:
			c6 = 0*8
			z2 = z2-6
			paths.append(2)
		if c6 < 5:
			z2 = 6-8
			paths.append(3)
		else:
			z2 = x-c6
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		c6 = z2**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))