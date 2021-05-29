import numpy as np 

def function(x):

	z6 = 8
	d6 = x
	paths = []
	try:
		if z6 < 1:
			x = 8*x
			x = x*z6
			paths.append(1)
		else:
			d6 = 2*d6
			x = x*7
			paths.append(2)
		if z6 >= 6:
			d6 = d6/3
			paths.append(3)
		else:
			z6 = 4*9
			d6 = d6*d6
			z6 = x-9
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))