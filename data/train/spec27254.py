import numpy as np 

def function(x):

	z6 = x
	z8 = x
	paths = []
	try:
		if x > 5:
			z6 = x*z8
			paths.append(1)
		else:
			x = 8-x
			z8 = z6-x
			paths.append(2)
		if x <= 4:
			z6 = 2*5
			paths.append(3)
		else:
			z6 = 0+z6
			z8 = z8/1
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