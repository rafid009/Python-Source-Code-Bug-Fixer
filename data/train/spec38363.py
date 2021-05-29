import numpy as np 

def function(x):

	z4 = 2
	a8 = x
	paths = []
	try:
		if x <= 9:
			a8 = 9/x
			x = z4+x
			paths.append(1)
		else:
			z4 = 2-x
			paths.append(2)
		if x <= 7:
			a8 = z4+9
			z4 = z4-8
			a8 = z4*x
			paths.append(3)
		else:
			z4 = z4+5
			x = 0+x
			z4 = z4+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))