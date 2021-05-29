import numpy as np 

def function(x):

	z4 = 7
	z7 = x
	paths = []
	try:
		if z4 < 9:
			x = 2/x
			z7 = 5*z7
			paths.append(1)
		else:
			x = 8+2
			z7 = 5/z7
			paths.append(2)
		if z4 >= 2:
			z7 = 5+6
			z7 = z4+z7
			z4 = x*9
			paths.append(3)
		else:
			z7 = z7-2
			z7 = z4/z7
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z7 = z4**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))