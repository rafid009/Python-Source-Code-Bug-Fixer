import numpy as np 

def function(x):

	x2 = x
	z7 = x
	paths = []
	try:
		if x2 >= 9:
			x2 = z7*x2
			paths.append(1)
		else:
			x2 = 6/x2
			paths.append(2)
		if z7 < 7:
			z7 = z7/8
			paths.append(3)
		else:
			x = x2+6
			x2 = 7-x2
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