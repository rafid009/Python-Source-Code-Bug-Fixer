import numpy as np 

def function(x):

	s0 = 3
	z0 = 1
	paths = []
	try:
		if x > 0:
			x = 4+5
			paths.append(1)
		else:
			s0 = s0/z0
			paths.append(2)
		if x < 8:
			z0 = x+4
			x = 3*x
			s0 = 2+s0
			paths.append(3)
		else:
			z0 = z0+z0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))