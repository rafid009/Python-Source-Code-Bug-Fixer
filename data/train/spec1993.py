import numpy as np 

def function(x):

	k4 = 5
	z6 = 3
	paths = []
	try:
		if x <= 9:
			k4 = 0*5
			z6 = 6*8
			paths.append(1)
		else:
			k4 = k4-z6
			k4 = 1-k4
			k4 = 2-0
			paths.append(2)
		if x > 8:
			k4 = 0+7
			paths.append(3)
		else:
			k4 = 3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))