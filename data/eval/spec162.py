import numpy as np 

def function(x):

	z7 = x
	w3 = x
	paths = []
	try:
		if z7 >= 0:
			z7 = 7/z7
			z7 = z7-3
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if z7 <= 1:
			w3 = w3+9
			x = x+5
			x = 4+x
			paths.append(3)
		else:
			z7 = z7*1
			w3 = 7-w3
			z7 = z7+x
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