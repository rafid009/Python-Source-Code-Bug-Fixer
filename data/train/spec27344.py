import numpy as np 

def function(x):

	z6 = 9
	c2 = 0
	x = x
	paths = []
	try:
		if z6 <= 9:
			z6 = x*1
			paths.append(1)
		else:
			z6 = z6/2
			c2 = c2/8
			paths.append(2)
		if z6 < 5:
			c2 = 8+c2
			z6 = z6-7
			z6 = z6*3
			paths.append(3)
		else:
			x = x-z6
			z6 = 2+z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))