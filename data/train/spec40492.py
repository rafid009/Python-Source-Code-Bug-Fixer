import numpy as np 

def function(x):

	z1 = x
	a7 = 9
	paths = []
	try:
		if a7 < 4:
			z1 = z1+2
			z1 = x+6
			z1 = 7/z1
			paths.append(1)
		else:
			a7 = a7-0
			a7 = x-8
			z1 = 4-z1
			paths.append(2)
		if a7 < 7:
			a7 = z1+a7
			z1 = 1*z1
			paths.append(3)
		else:
			a7 = 4/a7
			a7 = 5*a7
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))