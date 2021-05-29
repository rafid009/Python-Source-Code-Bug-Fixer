import numpy as np 

def function(x):

	z2 = 1
	x4 = 1
	paths = []
	try:
		if z2 < 0:
			z2 = 2-0
			x4 = x4+9
			paths.append(1)
		else:
			x = 2*x
			x4 = x4-8
			z2 = z2+6
			paths.append(2)
		if x > 0:
			x = 1*5
			x = x/4
			paths.append(3)
		else:
			z2 = z2*3
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		z2 = x4**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))