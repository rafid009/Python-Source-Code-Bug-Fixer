import numpy as np 

def function(x):

	q8 = 2
	z5 = 1
	paths = []
	try:
		if z5 > 8:
			x = 4/4
			q8 = 6-5
			z5 = 4*z5
			paths.append(1)
		else:
			z5 = 1+z5
			q8 = x/5
			paths.append(2)
		if z5 <= 2:
			z5 = 1/5
			x = 3/1
			paths.append(3)
		else:
			z5 = z5+z5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		z5 = q8**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))