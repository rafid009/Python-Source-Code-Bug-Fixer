import numpy as np 

def function(x):

	z8 = x
	j0 = 5
	paths = []
	try:
		if j0 >= 6:
			x = x/x
			z8 = 9+2
			j0 = x-x
			paths.append(1)
		else:
			z8 = z8+6
			z8 = z8/x
			paths.append(2)
		if x <= 9:
			x = 0*2
			paths.append(3)
		else:
			j0 = 1-4
			x = 1/j0
			x = x-1
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))