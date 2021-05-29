import numpy as np 

def function(x):

	z5 = x
	z1 = x
	paths = []
	try:
		if z1 > 9:
			z5 = 0*1
			x = x*5
			paths.append(1)
		else:
			z5 = z5-6
			z5 = x/x
			paths.append(2)
		if z1 >= 0:
			z1 = z1*1
			paths.append(3)
		else:
			x = z1+z1
			z5 = z5*1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z5 = z1**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))