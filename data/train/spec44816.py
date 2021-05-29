import numpy as np 

def function(x):

	z2 = 8
	c3 = 0
	paths = []
	try:
		if c3 < 9:
			z2 = z2-z2
			c3 = c3+6
			paths.append(1)
		else:
			c3 = 6-6
			z2 = 7/z2
			z2 = x+x
			paths.append(2)
		if z2 > 1:
			x = z2+x
			paths.append(3)
		else:
			z2 = 8/5
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