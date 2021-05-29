import numpy as np 

def function(x):

	z7 = 9
	e3 = 0
	paths = []
	try:
		if x <= 4:
			e3 = 1/1
			paths.append(1)
		else:
			z7 = z7/1
			x = x-0
			z7 = 2*z7
			paths.append(2)
		if z7 >= 4:
			x = x-z7
			paths.append(3)
		else:
			e3 = 2-e3
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