import numpy as np 

def function(x):

	l2 = 2
	z1 = 8
	paths = []
	try:
		if z1 < 2:
			z1 = x-1
			l2 = 6/2
			l2 = l2/9
			paths.append(1)
		else:
			l2 = x-4
			x = x+1
			paths.append(2)
		if z1 <= 0:
			l2 = l2*8
			z1 = z1+z1
			l2 = l2*1
			paths.append(3)
		else:
			x = 1-z1
			z1 = z1-z1
			z1 = z1/9
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