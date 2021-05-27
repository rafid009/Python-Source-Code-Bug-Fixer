import numpy as np 

def function(x):

	d8 = 4
	z0 = x
	paths = []
	try:
		if x <= 4:
			x = x+3
			paths.append(1)
		else:
			z0 = 1*z0
			paths.append(2)
		if d8 <= 3:
			z0 = x-z0
			x = 7-d8
			paths.append(3)
		else:
			x = x+4
			d8 = 3-z0
			z0 = 9/9
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