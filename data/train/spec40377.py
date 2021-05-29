import numpy as np 

def function(x):

	w3 = 1
	z7 = x
	paths = []
	try:
		if w3 >= 8:
			z7 = 6/z7
			w3 = 3+6
			w3 = w3+6
			paths.append(1)
		else:
			w3 = 0*5
			x = z7-x
			x = z7+w3
			paths.append(2)
		if z7 > 9:
			x = z7/8
			paths.append(3)
		else:
			z7 = 2/z7
			z7 = z7+4
			z7 = w3-x
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