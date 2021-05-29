import numpy as np 

def function(x):

	z6 = 3
	e3 = 2
	paths = []
	try:
		if z6 >= 2:
			x = x/4
			z6 = x+7
			paths.append(1)
		else:
			z6 = x/6
			x = 4*x
			e3 = x-e3
			paths.append(2)
		if e3 >= 1:
			x = z6/x
			paths.append(3)
		else:
			e3 = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))