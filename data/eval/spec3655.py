import numpy as np 

def function(x):

	s6 = x
	z5 = x
	x = 4
	paths = []
	try:
		if x >= 0:
			z5 = z5/1
			x = 9*x
			z5 = 4/z5
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if x >= 5:
			z5 = 2*z5
			x = x+8
			paths.append(3)
		else:
			z5 = z5-7
			x = x+6
			z5 = z5+8
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		z5 = s6**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))