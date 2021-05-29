import numpy as np 

def function(x):

	z0 = x
	n5 = x
	paths = []
	try:
		if n5 < 3:
			n5 = n5*1
			x = z0/x
			paths.append(1)
		else:
			x = 6-7
			x = x+x
			paths.append(2)
		if z0 < 9:
			n5 = 6-z0
			paths.append(3)
		else:
			z0 = 1/z0
			z0 = x/1
			n5 = 2*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))