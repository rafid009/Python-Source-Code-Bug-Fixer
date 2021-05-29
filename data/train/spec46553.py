import numpy as np 

def function(x):

	z0 = 1
	k6 = x
	paths = []
	try:
		if k6 >= 6:
			x = z0/k6
			x = 3/x
			k6 = z0*3
			paths.append(1)
		else:
			x = 4/4
			z0 = 9-4
			paths.append(2)
		if x <= 0:
			z0 = x/z0
			k6 = k6*k6
			x = z0/x
			paths.append(3)
		else:
			z0 = 7-x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		k6 = z0**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))