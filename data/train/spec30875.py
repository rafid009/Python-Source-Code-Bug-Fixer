import numpy as np 

def function(x):

	z0 = 8
	h8 = 9
	paths = []
	try:
		if h8 >= 8:
			z0 = 5*z0
			z0 = x*8
			paths.append(1)
		else:
			h8 = h8/x
			h8 = 0+h8
			z0 = z0+3
			paths.append(2)
		if x <= 4:
			x = x/5
			z0 = z0*9
			paths.append(3)
		else:
			z0 = h8/6
			h8 = 3+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))