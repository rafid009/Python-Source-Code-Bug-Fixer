import numpy as np 

def function(x):

	t0 = x
	z1 = x
	paths = []
	try:
		if z1 > 0:
			x = 4-x
			x = 1+x
			z1 = 6+z1
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if t0 < 4:
			z1 = 9-z1
			paths.append(3)
		else:
			z1 = 8*8
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