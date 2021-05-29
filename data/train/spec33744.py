import numpy as np 

def function(x):

	a4 = 0
	z7 = x
	paths = []
	try:
		if a4 < 2:
			x = 5/z7
			z7 = z7/6
			a4 = a4/1
			paths.append(1)
		else:
			a4 = a4+8
			z7 = 4-1
			paths.append(2)
		if z7 >= 0:
			x = x*5
			a4 = 7/z7
			paths.append(3)
		else:
			x = 8/x
			a4 = 7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))