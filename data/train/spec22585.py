import numpy as np 

def function(x):

	f7 = 9
	z0 = 4
	x = x
	paths = []
	try:
		if x < 3:
			z0 = z0-f7
			x = z0-0
			x = z0-x
			paths.append(1)
		else:
			f7 = 3-f7
			paths.append(2)
		if z0 >= 8:
			x = x*6
			paths.append(3)
		else:
			x = x/f7
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