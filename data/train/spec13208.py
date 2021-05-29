import numpy as np 

def function(x):

	v1 = 8
	z0 = 1
	paths = []
	try:
		if v1 > 2:
			x = 1-0
			paths.append(1)
		else:
			v1 = 5+v1
			v1 = 9+2
			x = x-z0
			paths.append(2)
		if z0 > 9:
			z0 = 4*z0
			v1 = 9/7
			paths.append(3)
		else:
			z0 = 2-4
			v1 = z0*v1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		z0 = v1**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))