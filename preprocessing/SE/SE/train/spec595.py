import numpy as np 

def function(x):

	z0 = x
	z7 = 1
	x = x
	paths = []
	try:
		if z0 <= 1:
			z7 = z7+0
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if z7 >= 3:
			z0 = 7+z7
			x = x+9
			paths.append(3)
		else:
			z7 = z7*1
			z7 = z7/z7
			z0 = 1+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))