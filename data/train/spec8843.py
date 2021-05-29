import numpy as np 

def function(x):

	y7 = 2
	z4 = 5
	paths = []
	try:
		if x >= 4:
			z4 = 8-y7
			z4 = z4-z4
			x = 6+x
			paths.append(1)
		else:
			z4 = y7/z4
			paths.append(2)
		if y7 < 0:
			x = 3+y7
			paths.append(3)
		else:
			z4 = x+7
			z4 = 3-z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))