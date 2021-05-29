import numpy as np 

def function(x):

	z5 = 9
	j0 = 8
	paths = []
	try:
		if x < 9:
			z5 = 9+7
			j0 = j0+8
			j0 = j0+2
			paths.append(1)
		else:
			x = 4-x
			j0 = j0*4
			paths.append(2)
		if j0 <= 8:
			x = x-9
			z5 = x/7
			z5 = j0+z5
			paths.append(3)
		else:
			j0 = 1+x
			j0 = j0+z5
			z5 = z5+8
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