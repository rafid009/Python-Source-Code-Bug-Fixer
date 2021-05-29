import numpy as np 

def function(x):

	k0 = x
	z6 = 1
	paths = []
	try:
		if k0 >= 9:
			k0 = 4*7
			paths.append(1)
		else:
			z6 = 0-9
			x = x/x
			x = x-8
			paths.append(2)
		if x < 6:
			z6 = z6-7
			x = x-x
			paths.append(3)
		else:
			k0 = 9/k0
			k0 = 3*k0
			z6 = z6-2
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		z6 = k0**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))