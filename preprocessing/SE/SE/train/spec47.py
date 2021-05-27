import numpy as np 

def function(x):

	z0 = x
	l3 = x
	paths = []
	try:
		if l3 > 2:
			x = 2+x
			l3 = 7/l3
			l3 = l3*l3
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if l3 < 8:
			l3 = 9*l3
			paths.append(3)
		else:
			z0 = l3/x
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