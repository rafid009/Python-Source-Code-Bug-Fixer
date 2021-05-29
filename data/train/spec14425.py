import numpy as np 

def function(x):

	z6 = 0
	e8 = 6
	paths = []
	try:
		if x <= 9:
			z6 = x*6
			e8 = e8-1
			paths.append(1)
		else:
			e8 = 0*e8
			e8 = z6+4
			paths.append(2)
		if x >= 6:
			z6 = z6*x
			paths.append(3)
		else:
			z6 = 1*z6
			x = x+4
			x = e8-9
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))