import numpy as np 

def function(x):

	z7 = 2
	k0 = x
	paths = []
	try:
		if k0 > 5:
			k0 = 3*5
			paths.append(1)
		else:
			z7 = z7+3
			paths.append(2)
		if x < 4:
			z7 = z7/z7
			k0 = k0/6
			x = 4-8
			paths.append(3)
		else:
			x = k0+z7
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