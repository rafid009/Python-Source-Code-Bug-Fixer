import numpy as np 

def function(x):

	z4 = x
	n1 = 2
	paths = []
	try:
		if x < 3:
			n1 = z4+n1
			x = x/4
			paths.append(1)
		else:
			z4 = z4*x
			x = n1/x
			paths.append(2)
		if z4 > 9:
			x = 5*n1
			paths.append(3)
		else:
			x = z4-x
			n1 = 1+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))