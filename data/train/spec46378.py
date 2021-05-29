import numpy as np 

def function(x):

	z9 = x
	y7 = x
	paths = []
	try:
		if x < 8:
			y7 = y7/5
			paths.append(1)
		else:
			z9 = 3/z9
			x = z9+7
			z9 = 4+4
			paths.append(2)
		if x >= 1:
			z9 = y7+y7
			z9 = z9*z9
			x = z9-9
			paths.append(3)
		else:
			z9 = 0/4
			z9 = y7/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))