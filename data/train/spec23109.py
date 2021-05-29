import numpy as np 

def function(x):

	v1 = 9
	z0 = 9
	paths = []
	try:
		if z0 >= 1:
			z0 = z0-x
			z0 = 8+x
			paths.append(1)
		else:
			x = z0/1
			x = 0+3
			v1 = 4-2
			paths.append(2)
		if x >= 4:
			z0 = 3*z0
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))