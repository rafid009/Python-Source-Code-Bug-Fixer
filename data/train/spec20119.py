import numpy as np 

def function(x):

	q5 = 3
	z0 = 8
	paths = []
	try:
		if q5 <= 1:
			q5 = q5-2
			z0 = 9/z0
			paths.append(1)
		else:
			z0 = z0+2
			paths.append(2)
		if q5 < 2:
			z0 = z0-5
			paths.append(3)
		else:
			q5 = q5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))