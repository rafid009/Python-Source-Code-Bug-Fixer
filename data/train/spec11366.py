import numpy as np 

def function(x):

	z7 = 8
	n7 = 5
	paths = []
	try:
		if n7 <= 5:
			x = 8-x
			n7 = n7-0
			paths.append(1)
		else:
			z7 = x+n7
			z7 = 8*z7
			z7 = z7-n7
			paths.append(2)
		if x <= 1:
			n7 = n7-n7
			x = x+3
			z7 = 9-z7
			paths.append(3)
		else:
			x = 0/6
			n7 = 0-n7
			n7 = 7+x
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