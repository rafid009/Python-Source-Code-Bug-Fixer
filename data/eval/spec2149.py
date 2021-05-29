import numpy as np 

def function(x):

	e6 = 6
	z1 = 5
	paths = []
	try:
		if x >= 7:
			z1 = 2*3
			e6 = e6+7
			paths.append(1)
		else:
			z1 = 6/z1
			x = 8*x
			e6 = e6-5
			paths.append(2)
		if e6 > 9:
			e6 = z1-9
			e6 = e6-6
			paths.append(3)
		else:
			z1 = x-z1
			x = z1-x
			z1 = z1-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))