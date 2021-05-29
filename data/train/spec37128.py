import numpy as np 

def function(x):

	u4 = 1
	z6 = x
	paths = []
	try:
		if x >= 0:
			z6 = z6+5
			paths.append(1)
		else:
			z6 = 9+9
			paths.append(2)
		if z6 < 4:
			z6 = 0*z6
			paths.append(3)
		else:
			z6 = 4/z6
			x = x-5
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