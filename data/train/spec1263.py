import numpy as np 

def function(x):

	q9 = 6
	z5 = x
	paths = []
	try:
		if x <= 0:
			x = 8*q9
			q9 = q9+0
			x = q9*8
			paths.append(1)
		else:
			z5 = 4*x
			z5 = z5-5
			z5 = 7+3
			paths.append(2)
		if z5 <= 0:
			x = x/9
			paths.append(3)
		else:
			z5 = 4+z5
			z5 = z5*x
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