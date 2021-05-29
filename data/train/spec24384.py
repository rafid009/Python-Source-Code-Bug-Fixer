import numpy as np 

def function(x):

	a6 = 9
	z1 = x
	x = 7
	paths = []
	try:
		if z1 > 9:
			z1 = 1+4
			x = 8/5
			paths.append(1)
		else:
			x = 6/z1
			paths.append(2)
		if a6 < 7:
			a6 = 9*a6
			paths.append(3)
		else:
			x = a6*x
			a6 = 1-a6
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