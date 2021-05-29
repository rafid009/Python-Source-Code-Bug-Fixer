import numpy as np 

def function(x):

	z0 = 5
	q7 = x
	paths = []
	try:
		if z0 > 6:
			q7 = q7*9
			x = x+x
			paths.append(1)
		else:
			z0 = q7*3
			paths.append(2)
		if q7 > 8:
			z0 = 1-3
			q7 = 7*6
			paths.append(3)
		else:
			q7 = q7-6
			z0 = x-7
			z0 = x/z0
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		z0 = q7**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))