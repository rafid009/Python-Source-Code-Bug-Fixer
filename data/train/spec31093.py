import numpy as np 

def function(x):

	e3 = 0
	z7 = x
	paths = []
	try:
		if z7 <= 2:
			e3 = 9-e3
			e3 = 0/e3
			e3 = 1-z7
			paths.append(1)
		else:
			x = 3-e3
			z7 = z7/5
			paths.append(2)
		if z7 > 6:
			z7 = z7/z7
			paths.append(3)
		else:
			e3 = 6*e3
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		e3 = z7**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))