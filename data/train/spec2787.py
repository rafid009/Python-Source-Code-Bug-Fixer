import numpy as np 

def function(x):

	z6 = x
	q1 = x
	paths = []
	try:
		if q1 >= 7:
			z6 = 6*z6
			paths.append(1)
		else:
			z6 = 6-x
			z6 = z6/4
			x = 0*x
			paths.append(2)
		if q1 >= 1:
			z6 = 3+z6
			paths.append(3)
		else:
			z6 = 0-9
			z6 = z6-9
			q1 = q1-x
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		z6 = q1**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))