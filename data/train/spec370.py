import numpy as np 

def function(x):

	n4 = 5
	z6 = 3
	paths = []
	try:
		if z6 < 1:
			n4 = x*z6
			z6 = 8*z6
			n4 = 1-9
			paths.append(1)
		else:
			z6 = z6*3
			x = x/x
			paths.append(2)
		if z6 > 4:
			z6 = 8-z6
			paths.append(3)
		else:
			z6 = 8+2
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