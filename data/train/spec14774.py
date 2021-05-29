import numpy as np 

def function(x):

	l1 = x
	z0 = 2
	paths = []
	try:
		if x < 6:
			z0 = l1/5
			z0 = z0+6
			paths.append(1)
		else:
			x = z0-l1
			x = 7-0
			paths.append(2)
		if l1 < 4:
			l1 = 3*l1
			paths.append(3)
		else:
			x = z0+l1
			x = x/5
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