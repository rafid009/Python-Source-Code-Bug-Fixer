import numpy as np 

def function(x):

	c1 = 5
	z1 = 4
	paths = []
	try:
		if x < 3:
			c1 = 8-c1
			paths.append(1)
		else:
			z1 = 9-z1
			paths.append(2)
		if z1 < 9:
			z1 = z1/c1
			x = x+c1
			paths.append(3)
		else:
			x = x*3
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