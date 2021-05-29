import numpy as np 

def function(x):

	z7 = x
	e5 = 4
	paths = []
	try:
		if z7 > 0:
			e5 = z7-x
			paths.append(1)
		else:
			e5 = e5*x
			paths.append(2)
		if z7 <= 3:
			z7 = 4-z7
			paths.append(3)
		else:
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