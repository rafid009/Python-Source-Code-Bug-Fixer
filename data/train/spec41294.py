import numpy as np 

def function(x):

	z0 = 6
	p3 = 6
	paths = []
	try:
		if x > 1:
			p3 = p3-p3
			p3 = 7*p3
			paths.append(1)
		else:
			z0 = z0-8
			p3 = z0*p3
			paths.append(2)
		if p3 >= 1:
			x = 0*x
			paths.append(3)
		else:
			z0 = z0-5
			p3 = 7+0
			x = x-p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))