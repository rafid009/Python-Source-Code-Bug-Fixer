import numpy as np 

def function(x):

	z0 = 8
	c7 = 9
	paths = []
	try:
		if x < 6:
			x = z0+8
			z0 = z0-9
			c7 = z0-1
			paths.append(1)
		else:
			z0 = x+7
			x = 2+c7
			paths.append(2)
		if x > 5:
			c7 = c7-6
			paths.append(3)
		else:
			z0 = z0+1
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