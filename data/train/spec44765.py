import numpy as np 

def function(x):

	y2 = 7
	z9 = x
	paths = []
	try:
		if x >= 9:
			y2 = 5+7
			z9 = z9*9
			paths.append(1)
		else:
			x = 3-4
			paths.append(2)
		if x <= 1:
			y2 = y2*6
			z9 = 3/z9
			paths.append(3)
		else:
			z9 = y2-z9
			z9 = z9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))