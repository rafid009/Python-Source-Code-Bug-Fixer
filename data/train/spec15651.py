import numpy as np 

def function(x):

	z0 = 4
	h5 = x
	paths = []
	try:
		if h5 >= 4:
			z0 = 1*z0
			paths.append(1)
		else:
			z0 = z0/9
			paths.append(2)
		if h5 <= 5:
			z0 = z0-4
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))