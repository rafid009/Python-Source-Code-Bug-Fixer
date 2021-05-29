import numpy as np 

def function(x):

	z5 = 2
	z6 = x
	x = x
	paths = []
	try:
		if z6 > 0:
			x = x*5
			paths.append(1)
		else:
			z5 = z5*z5
			x = x+9
			z5 = z6-9
			paths.append(2)
		if x < 7:
			z6 = z6/9
			x = x*x
			paths.append(3)
		else:
			z5 = 1+x
			z5 = 8-z6
			z5 = x+z6
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