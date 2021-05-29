import numpy as np 

def function(x):

	w0 = 5
	z7 = x
	x = 6
	paths = []
	try:
		if z7 < 3:
			w0 = 7/w0
			paths.append(1)
		else:
			x = z7+3
			paths.append(2)
		if z7 > 1:
			z7 = 0+z7
			z7 = z7-1
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))