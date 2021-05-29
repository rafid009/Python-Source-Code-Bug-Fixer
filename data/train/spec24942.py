import numpy as np 

def function(x):

	x4 = x
	z2 = x
	paths = []
	try:
		if z2 > 6:
			z2 = 2*x4
			x = z2+3
			paths.append(1)
		else:
			x4 = z2/6
			x = x4*6
			x = 5+z2
			paths.append(2)
		if z2 < 3:
			x4 = 1*x4
			paths.append(3)
		else:
			x = x+7
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