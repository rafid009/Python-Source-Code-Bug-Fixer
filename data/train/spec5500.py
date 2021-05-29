import numpy as np 

def function(x):

	z6 = x
	z1 = x
	paths = []
	try:
		if x >= 6:
			z1 = z1*x
			paths.append(1)
		else:
			z6 = 1*z1
			z6 = 1-z6
			paths.append(2)
		if z6 >= 4:
			z6 = 6*z1
			z6 = x*z6
			paths.append(3)
		else:
			x = x+6
			z6 = 5+x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))