import numpy as np 

def function(x):

	q8 = 0
	z0 = 7
	paths = []
	try:
		if z0 >= 7:
			x = x+z0
			paths.append(1)
		else:
			q8 = q8-2
			x = 6+x
			paths.append(2)
		if z0 >= 5:
			q8 = q8-q8
			z0 = q8-x
			z0 = z0*6
			paths.append(3)
		else:
			x = q8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))