import numpy as np 

def function(x):

	y4 = 0
	z2 = 8
	paths = []
	try:
		if y4 >= 1:
			x = 6+9
			x = 9+8
			paths.append(1)
		else:
			z2 = z2*z2
			x = x-0
			paths.append(2)
		if z2 > 0:
			z2 = z2*8
			x = x-9
			paths.append(3)
		else:
			z2 = 4-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))