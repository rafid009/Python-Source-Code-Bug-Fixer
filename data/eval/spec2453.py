import numpy as np 

def function(x):

	x4 = 3
	z1 = 6
	paths = []
	try:
		if x < 3:
			z1 = z1-0
			z1 = x4-7
			x4 = 1*x4
			paths.append(1)
		else:
			z1 = z1*1
			paths.append(2)
		if z1 >= 2:
			x = 0-x4
			x = x/2
			paths.append(3)
		else:
			x4 = x4-3
			z1 = z1*z1
			z1 = x*z1
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