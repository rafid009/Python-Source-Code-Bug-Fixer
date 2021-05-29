import numpy as np 

def function(x):

	z0 = x
	r8 = x
	paths = []
	try:
		if z0 <= 4:
			r8 = 7/3
			r8 = 6/r8
			paths.append(1)
		else:
			z0 = z0-z0
			paths.append(2)
		if z0 < 5:
			r8 = 3/r8
			r8 = 1+8
			paths.append(3)
		else:
			x = 6-z0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))