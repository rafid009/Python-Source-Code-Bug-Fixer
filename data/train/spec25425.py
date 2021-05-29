import numpy as np 

def function(x):

	e7 = 0
	z8 = 4
	paths = []
	try:
		if x <= 0:
			e7 = 8-x
			z8 = 6+z8
			paths.append(1)
		else:
			x = 8-x
			x = z8+0
			x = 2*x
			paths.append(2)
		if e7 >= 0:
			e7 = e7/4
			e7 = 1+8
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))