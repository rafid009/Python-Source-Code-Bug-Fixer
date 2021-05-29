import numpy as np 

def function(x):

	a6 = 7
	z1 = x
	paths = []
	try:
		if z1 >= 3:
			a6 = a6/1
			paths.append(1)
		else:
			z1 = a6+6
			x = 2-x
			paths.append(2)
		if x > 3:
			x = x/z1
			z1 = 5-9
			x = 8-1
			paths.append(3)
		else:
			z1 = 1+z1
			a6 = a6*a6
			z1 = z1/4
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