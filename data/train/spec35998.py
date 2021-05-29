import numpy as np 

def function(x):

	c3 = 8
	z6 = x
	x = x
	paths = []
	try:
		if z6 > 6:
			c3 = 5/c3
			paths.append(1)
		else:
			z6 = z6*2
			z6 = 2-9
			paths.append(2)
		if z6 <= 9:
			c3 = c3+7
			z6 = 2/2
			paths.append(3)
		else:
			x = c3-x
			c3 = c3*4
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