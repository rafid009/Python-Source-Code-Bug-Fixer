import numpy as np 

def function(x):

	n4 = 8
	z7 = 3
	paths = []
	try:
		if z7 <= 0:
			n4 = x/n4
			paths.append(1)
		else:
			z7 = z7*4
			z7 = z7-1
			paths.append(2)
		if x < 6:
			n4 = n4*x
			paths.append(3)
		else:
			n4 = x*n4
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