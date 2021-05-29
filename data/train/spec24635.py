import numpy as np 

def function(x):

	q3 = x
	z0 = 8
	paths = []
	try:
		if z0 <= 7:
			z0 = q3/z0
			z0 = z0-1
			q3 = q3-z0
			paths.append(1)
		else:
			x = 0+1
			x = 6*x
			z0 = z0+q3
			paths.append(2)
		if x >= 5:
			q3 = z0/q3
			x = 7*q3
			x = 4/q3
			paths.append(3)
		else:
			q3 = q3-4
			z0 = z0/x
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))