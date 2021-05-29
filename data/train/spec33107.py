import numpy as np 

def function(x):

	z0 = 6
	q4 = x
	x = 4
	paths = []
	try:
		if q4 > 2:
			x = x*2
			paths.append(1)
		else:
			x = q4*6
			paths.append(2)
		if x < 6:
			z0 = z0-8
			q4 = 7*5
			paths.append(3)
		else:
			q4 = q4/x
			z0 = z0-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))