import numpy as np 

def function(x):

	z7 = 3
	x3 = x
	paths = []
	try:
		if z7 >= 8:
			x3 = x3*7
			paths.append(1)
		else:
			x3 = 7+x3
			z7 = z7-9
			z7 = x-7
			paths.append(2)
		if x3 > 9:
			x3 = z7/x3
			x = 7-x
			paths.append(3)
		else:
			x = 1*x
			z7 = 5*z7
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