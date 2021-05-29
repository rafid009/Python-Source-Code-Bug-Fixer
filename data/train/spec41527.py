import numpy as np 

def function(x):

	z5 = 8
	m4 = 4
	paths = []
	try:
		if z5 < 6:
			x = 1/x
			z5 = z5-8
			x = z5+5
			paths.append(1)
		else:
			m4 = 7-z5
			z5 = 9*x
			x = 5/8
			paths.append(2)
		if z5 >= 7:
			z5 = z5-4
			paths.append(3)
		else:
			m4 = 5*m4
			x = z5-5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))