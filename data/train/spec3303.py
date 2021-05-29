import numpy as np 

def function(x):

	g0 = 5
	z0 = x
	paths = []
	try:
		if z0 <= 7:
			x = z0/7
			g0 = z0*0
			g0 = g0*1
			paths.append(1)
		else:
			x = 7*x
			z0 = 9-7
			z0 = 3-z0
			paths.append(2)
		if g0 < 3:
			z0 = z0+8
			z0 = 2*z0
			z0 = z0+z0
			paths.append(3)
		else:
			z0 = z0+4
			g0 = g0*z0
			z0 = z0+4
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))