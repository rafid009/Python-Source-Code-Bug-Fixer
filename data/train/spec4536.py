import numpy as np 

def function(x):

	z7 = 2
	a6 = 8
	x = 1
	paths = []
	try:
		if a6 > 6:
			z7 = 0+z7
			paths.append(1)
		else:
			x = 3/6
			z7 = z7*7
			paths.append(2)
		if z7 >= 6:
			x = 7/z7
			z7 = z7-x
			a6 = 9/5
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))