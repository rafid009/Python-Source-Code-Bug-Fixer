import numpy as np 

def function(x):

	z1 = 7
	l2 = x
	paths = []
	try:
		if z1 <= 9:
			l2 = 9+8
			z1 = z1-z1
			x = x-3
			paths.append(1)
		else:
			x = x-x
			x = x-0
			x = x/l2
			paths.append(2)
		if x <= 3:
			x = 6*x
			x = x-3
			x = z1-1
			paths.append(3)
		else:
			z1 = z1-9
			l2 = l2/z1
			x = z1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))