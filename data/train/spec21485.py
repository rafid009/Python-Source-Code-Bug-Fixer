import numpy as np 

def function(x):

	x5 = x
	z5 = 0
	x = x
	paths = []
	try:
		if z5 < 3:
			z5 = z5+2
			x5 = z5*x5
			paths.append(1)
		else:
			x = 6+2
			x5 = x5*7
			x5 = x5+x
			paths.append(2)
		if z5 <= 7:
			z5 = 6*3
			x5 = 8-x5
			x5 = 3-x5
			paths.append(3)
		else:
			z5 = 7*x
			x = x+8
			x = 7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))