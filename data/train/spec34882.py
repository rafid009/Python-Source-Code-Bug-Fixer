import numpy as np 

def function(x):

	z7 = x
	e8 = 6
	paths = []
	try:
		if e8 <= 6:
			x = x-2
			e8 = 5+e8
			paths.append(1)
		else:
			z7 = z7/1
			paths.append(2)
		if z7 <= 8:
			e8 = e8-0
			paths.append(3)
		else:
			z7 = e8+4
			z7 = z7/z7
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