import numpy as np 

def function(x):

	z5 = 7
	o3 = 6
	paths = []
	try:
		if x < 2:
			z5 = x-z5
			z5 = z5+2
			o3 = 1+o3
			paths.append(1)
		else:
			x = 0*3
			x = x/o3
			paths.append(2)
		if z5 <= 1:
			x = z5/z5
			o3 = 7/z5
			paths.append(3)
		else:
			o3 = z5+3
			z5 = x-z5
			o3 = 4+8
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		z5 = o3**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))