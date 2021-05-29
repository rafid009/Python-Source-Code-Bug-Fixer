import numpy as np 

def function(x):

	z0 = 2
	p0 = x
	paths = []
	try:
		if x >= 7:
			x = x/4
			p0 = x-5
			paths.append(1)
		else:
			p0 = p0/8
			p0 = 6+8
			x = z0-x
			paths.append(2)
		if x < 3:
			p0 = x-0
			z0 = p0+z0
			x = p0-x
			paths.append(3)
		else:
			z0 = z0*9
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