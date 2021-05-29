import numpy as np 

def function(x):

	z7 = 0
	e6 = x
	paths = []
	try:
		if z7 < 1:
			e6 = 6*e6
			z7 = 1-z7
			paths.append(1)
		else:
			x = 4+e6
			e6 = 3/6
			paths.append(2)
		if x > 9:
			e6 = e6/x
			e6 = e6-z7
			paths.append(3)
		else:
			z7 = z7-e6
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