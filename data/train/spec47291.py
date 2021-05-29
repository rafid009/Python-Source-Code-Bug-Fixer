import numpy as np 

def function(x):

	x0 = x
	z9 = 1
	paths = []
	try:
		if x0 < 1:
			z9 = 3-x
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x > 5:
			x0 = 6/x0
			z9 = z9*z9
			paths.append(3)
		else:
			x = z9+4
			x = 6-z9
			x0 = x0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))