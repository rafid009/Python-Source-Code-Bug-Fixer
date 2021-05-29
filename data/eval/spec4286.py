import numpy as np 

def function(x):

	z0 = x
	f9 = 4
	paths = []
	try:
		if z0 > 1:
			z0 = z0/3
			f9 = f9-5
			paths.append(1)
		else:
			x = x+5
			x = x+1
			paths.append(2)
		if x >= 1:
			z0 = z0+0
			f9 = f9+8
			paths.append(3)
		else:
			z0 = f9/f9
			f9 = f9+4
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