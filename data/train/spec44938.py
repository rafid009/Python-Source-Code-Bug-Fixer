import numpy as np 

def function(x):

	z7 = 6
	n1 = x
	paths = []
	try:
		if x <= 9:
			x = 0*4
			x = x-2
			x = x/5
			paths.append(1)
		else:
			z7 = z7*z7
			paths.append(2)
		if x <= 5:
			z7 = 7-4
			x = x+n1
			z7 = n1/x
			paths.append(3)
		else:
			z7 = 5/1
			n1 = x+8
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