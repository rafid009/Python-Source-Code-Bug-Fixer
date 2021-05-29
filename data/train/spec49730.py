import numpy as np 

def function(x):

	z1 = x
	z4 = 8
	paths = []
	try:
		if z1 <= 5:
			x = z1/6
			paths.append(1)
		else:
			z1 = 1/5
			paths.append(2)
		if z1 <= 6:
			z1 = z1/z4
			z1 = 4/4
			paths.append(3)
		else:
			x = 0*x
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