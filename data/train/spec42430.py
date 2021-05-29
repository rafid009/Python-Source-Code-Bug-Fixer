import numpy as np 

def function(x):

	a7 = x
	z4 = 2
	paths = []
	try:
		if x <= 6:
			a7 = 0-a7
			z4 = 7*z4
			z4 = z4-1
			paths.append(1)
		else:
			x = x*x
			z4 = z4/a7
			z4 = z4+2
			paths.append(2)
		if x <= 8:
			z4 = 5*2
			a7 = a7-z4
			paths.append(3)
		else:
			z4 = 6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))