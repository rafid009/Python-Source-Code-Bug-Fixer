import numpy as np 

def function(x):

	x3 = x
	z5 = 1
	paths = []
	try:
		if x < 8:
			z5 = z5-x3
			z5 = 6-x3
			z5 = z5-0
			paths.append(1)
		else:
			z5 = 3+z5
			x = 8+x
			x = z5-0
			paths.append(2)
		if x3 < 4:
			x = x+1
			z5 = 8*x3
			x = x/x
			paths.append(3)
		else:
			z5 = 7/z5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		z5 = x3**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))