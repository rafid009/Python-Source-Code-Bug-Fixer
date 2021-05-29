import numpy as np 

def function(x):

	z4 = 1
	paths = []
	try:
		if z4 < 1:
			x = 1-0
			z4 = z4*3
			z4 = z4-z4
			paths.append(1)
		else:
			z4 = z4*2
			paths.append(2)
		if x >= 1:
			z4 = 0-2
			paths.append(3)
		else:
			z4 = 2-5
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))