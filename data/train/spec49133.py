import numpy as np 

def function(x):

	z0 = x
	c3 = 4
	paths = []
	try:
		if x <= 0:
			x = z0+x
			c3 = 1+c3
			paths.append(1)
		else:
			c3 = c3-1
			paths.append(2)
		if z0 < 8:
			z0 = z0-c3
			paths.append(3)
		else:
			c3 = c3/c3
			z0 = c3/9
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))