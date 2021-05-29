import numpy as np 

def function(x):

	z0 = 6
	e5 = x
	paths = []
	try:
		if x > 6:
			x = x-2
			paths.append(1)
		else:
			e5 = e5/e5
			paths.append(2)
		if x > 0:
			x = x*e5
			e5 = e5/z0
			paths.append(3)
		else:
			e5 = e5-z0
			z0 = 8-z0
			e5 = e5-9
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))