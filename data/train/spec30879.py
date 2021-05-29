import numpy as np 

def function(x):

	z5 = 6
	j0 = 9
	paths = []
	try:
		if x <= 6:
			z5 = 1/z5
			j0 = j0/6
			paths.append(1)
		else:
			j0 = 1-3
			paths.append(2)
		if j0 > 9:
			j0 = 9/9
			x = x/9
			paths.append(3)
		else:
			x = 8*x
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