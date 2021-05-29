import numpy as np 

def function(x):

	l4 = 2
	z5 = 4
	paths = []
	try:
		if x >= 0:
			z5 = z5+z5
			l4 = 8-l4
			l4 = 0+z5
			paths.append(1)
		else:
			x = z5/2
			paths.append(2)
		if x > 7:
			z5 = 5+1
			paths.append(3)
		else:
			l4 = x-7
			z5 = z5-z5
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		z5 = l4**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))