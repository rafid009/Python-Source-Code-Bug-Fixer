import numpy as np 

def function(x):

	z0 = 5
	f0 = x
	paths = []
	try:
		if f0 > 7:
			z0 = 1*f0
			f0 = 2-4
			paths.append(1)
		else:
			x = 5*f0
			paths.append(2)
		if f0 <= 9:
			x = 7+7
			z0 = 3-f0
			f0 = x-z0
			paths.append(3)
		else:
			z0 = z0+z0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		z0 = f0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))