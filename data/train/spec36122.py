import numpy as np 

def function(x):

	z4 = 7
	a8 = x
	paths = []
	try:
		if a8 >= 0:
			z4 = 0*z4
			z4 = 1-a8
			a8 = a8/a8
			paths.append(1)
		else:
			x = 1/5
			z4 = z4+a8
			paths.append(2)
		if x > 6:
			x = x+z4
			a8 = 8*a8
			x = 2+a8
			paths.append(3)
		else:
			z4 = 0-z4
			z4 = 2-z4
			x = x+2
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		a8 = z4**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))