import numpy as np 

def function(x):

	v2 = 6
	z4 = 0
	paths = []
	try:
		if z4 >= 7:
			x = x-9
			paths.append(1)
		else:
			z4 = 3+z4
			z4 = 0*4
			paths.append(2)
		if v2 <= 2:
			v2 = 1/v2
			v2 = 3*v2
			paths.append(3)
		else:
			z4 = v2+z4
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))