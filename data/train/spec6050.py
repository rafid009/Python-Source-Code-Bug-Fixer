import numpy as np 

def function(x):

	z0 = 9
	z4 = x
	paths = []
	try:
		if x < 7:
			z4 = x-9
			z4 = 3*z0
			z0 = x/z4
			paths.append(1)
		else:
			z0 = z0+3
			x = x*6
			z0 = 5-7
			paths.append(2)
		if z0 > 2:
			z4 = z4/z4
			paths.append(3)
		else:
			z4 = 4*z4
			x = x/4
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))