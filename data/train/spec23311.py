import numpy as np 

def function(x):

	z4 = 0
	u2 = x
	paths = []
	try:
		if z4 > 9:
			z4 = z4/3
			x = x-3
			paths.append(1)
		else:
			u2 = 8/u2
			z4 = 8+z4
			paths.append(2)
		if x < 6:
			u2 = 6*x
			paths.append(3)
		else:
			x = 8/x
			z4 = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))