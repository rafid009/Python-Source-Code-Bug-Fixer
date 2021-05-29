import numpy as np 

def function(x):

	p4 = 2
	z0 = x
	paths = []
	try:
		if z0 > 2:
			z0 = z0*1
			p4 = 4-p4
			paths.append(1)
		else:
			p4 = p4*x
			z0 = p4+0
			paths.append(2)
		if p4 > 1:
			z0 = 9*z0
			z0 = 0/z0
			paths.append(3)
		else:
			x = x-9
			z0 = 4/z0
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