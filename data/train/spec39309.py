import numpy as np 

def function(x):

	z0 = 4
	f2 = x
	paths = []
	try:
		if x >= 2:
			z0 = z0+8
			z0 = z0+3
			paths.append(1)
		else:
			z0 = 9+0
			f2 = f2+0
			z0 = 0+z0
			paths.append(2)
		if x < 0:
			z0 = 7-5
			paths.append(3)
		else:
			x = 1/x
			f2 = 5+2
			x = x*3
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))