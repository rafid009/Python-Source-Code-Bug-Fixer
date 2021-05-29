import numpy as np 

def function(x):

	z5 = 1
	d1 = x
	paths = []
	try:
		if z5 < 0:
			z5 = 5*z5
			d1 = d1/x
			d1 = 0+2
			paths.append(1)
		else:
			x = 0+d1
			paths.append(2)
		if x <= 1:
			z5 = 3-z5
			paths.append(3)
		else:
			z5 = 3/2
			x = x+0
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		z5 = d1**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))