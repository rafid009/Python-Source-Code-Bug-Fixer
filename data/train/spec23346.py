import numpy as np 

def function(x):

	a7 = 1
	z8 = x
	paths = []
	try:
		if a7 > 9:
			x = a7/x
			a7 = 2/5
			a7 = 0-5
			paths.append(1)
		else:
			a7 = x/4
			paths.append(2)
		if z8 <= 5:
			z8 = z8/1
			x = z8-9
			paths.append(3)
		else:
			x = 2*x
			z8 = 9*z8
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		z8 = a7**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))