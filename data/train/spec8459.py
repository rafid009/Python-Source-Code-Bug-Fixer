import numpy as np 

def function(x):

	a0 = 4
	z4 = 2
	paths = []
	try:
		if a0 > 7:
			x = 0-x
			z4 = 9/a0
			a0 = a0-5
			paths.append(1)
		else:
			a0 = 9/a0
			paths.append(2)
		if x < 7:
			z4 = 5*z4
			z4 = 2+5
			paths.append(3)
		else:
			z4 = z4-a0
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