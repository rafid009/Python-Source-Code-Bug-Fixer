import numpy as np 

def function(x):

	z0 = x
	p2 = x
	x = x
	paths = []
	try:
		if p2 < 6:
			x = 4*x
			paths.append(1)
		else:
			p2 = 9-p2
			z0 = z0/4
			x = z0*x
			paths.append(2)
		if z0 > 7:
			p2 = z0-p2
			paths.append(3)
		else:
			z0 = z0+2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		z0 = p2**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))