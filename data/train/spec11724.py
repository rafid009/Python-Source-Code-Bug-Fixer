import numpy as np 

def function(x):

	g9 = x
	z0 = x
	paths = []
	try:
		if x > 0:
			x = x*x
			z0 = 5/z0
			paths.append(1)
		else:
			x = g9*x
			paths.append(2)
		if z0 >= 9:
			z0 = z0/8
			g9 = z0*3
			paths.append(3)
		else:
			x = 0-9
			g9 = g9-3
			z0 = z0*8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		z0 = g9**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))