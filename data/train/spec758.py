import numpy as np 

def function(x):

	z0 = x
	a8 = 6
	x = 1
	paths = []
	try:
		if a8 <= 1:
			z0 = 3*a8
			paths.append(1)
		else:
			x = x*x
			x = 7/x
			paths.append(2)
		if a8 >= 4:
			a8 = 8*a8
			x = x-8
			z0 = 2*4
			paths.append(3)
		else:
			a8 = a8/6
			a8 = 8+1
			x = x+x
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