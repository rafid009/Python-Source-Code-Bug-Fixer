import numpy as np 

def function(x):

	v1 = 6
	z5 = 3
	paths = []
	try:
		if z5 <= 0:
			x = x*9
			x = 4-x
			v1 = z5/v1
			paths.append(1)
		else:
			x = x*5
			z5 = z5*v1
			paths.append(2)
		if v1 > 2:
			x = x/7
			paths.append(3)
		else:
			z5 = z5+z5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))