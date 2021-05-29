import numpy as np 

def function(x):

	n6 = x
	z7 = x
	paths = []
	try:
		if n6 < 5:
			z7 = z7*z7
			z7 = 4-z7
			z7 = z7*n6
			paths.append(1)
		else:
			n6 = n6-n6
			n6 = 3*n6
			x = 1-x
			paths.append(2)
		if z7 >= 1:
			n6 = 1*1
			n6 = n6-x
			z7 = z7/n6
			paths.append(3)
		else:
			n6 = n6*7
			z7 = 7+z7
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