import numpy as np 

def function(x):

	z2 = 5
	x8 = 9
	paths = []
	try:
		if z2 > 3:
			x8 = 6*z2
			z2 = z2-4
			paths.append(1)
		else:
			x = 3*z2
			z2 = 0/z2
			paths.append(2)
		if x8 < 5:
			x = 9/x
			x8 = x8/4
			paths.append(3)
		else:
			x8 = z2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))