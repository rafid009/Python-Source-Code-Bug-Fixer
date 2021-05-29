import numpy as np 

def function(x):

	n4 = 9
	z0 = x
	paths = []
	try:
		if n4 >= 3:
			x = 2-7
			x = 4*x
			n4 = n4/1
			paths.append(1)
		else:
			n4 = 7/4
			paths.append(2)
		if z0 < 4:
			n4 = 0-z0
			paths.append(3)
		else:
			x = x*9
			z0 = 4/7
			x = z0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))